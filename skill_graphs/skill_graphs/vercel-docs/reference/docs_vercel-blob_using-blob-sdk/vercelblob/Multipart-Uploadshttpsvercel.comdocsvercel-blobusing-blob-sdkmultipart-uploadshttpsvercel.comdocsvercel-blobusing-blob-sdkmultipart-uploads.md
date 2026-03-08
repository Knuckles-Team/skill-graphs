##  [Multipart Uploads](https://vercel.com/docs/vercel-blob/using-blob-sdk#multipart-uploads)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#multipart-uploads)
When uploading large files you should use multipart uploads to have a more reliable upload process. A multipart upload splits the file into multiple parts, uploads them in parallel and retries failed parts. This process consists of three phases: creating a multipart upload, uploading the parts and completing the upload. `@vercel/blob` offers three different ways to create multipart uploads:
###  [Automatic](https://vercel.com/docs/vercel-blob/using-blob-sdk#automatic)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#automatic)
This method has everything baked in and is easiest to use. It's part of the `put` and `upload` API's. Under the hood it will start the upload, split your file into multiple parts with the same size, upload them in parallel and complete the upload.
TypeScriptPython
```
const blob = await put('large-movie.mp4', file, {
  access: 'private' /* or 'public' */,
  multipart: true,
});
```

```
from vercel.blob import BlobClient

client = BlobClient()

with open("large-movie.mp4", "rb") as f:
    file_data = f.read()

blob = client.put(
    "videos/large-movie.mp4",
    file_data,
    access="private",  # or "public",
    content_type="video/mp4",
)
```

###  [Manual](https://vercel.com/docs/vercel-blob/using-blob-sdk#manual)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#manual)
This method gives you full control over the multipart upload process. It consists of three phases:
Phase 1: Create a multipart upload
TypeScriptPython
```
const multipartUpload = await createMultipartUpload(pathname, options);
```

```
from vercel.blob import create_multipart_upload

multipart_upload = create_multipart_upload(
    "videos/intro.mp4",
    access="private",  # or "public",
    content_type="video/mp4",
    add_random_suffix=True,
)
```

`createMultipartUpload` accepts the following parameters:
  * `pathname`: (Required) A string specifying the path inside the blob store. This will be the base value of the return URL and includes the filename and extension.
  * `options`: (Required) A `JSON` object with the following required and optional parameters:


Parameter | Required | Values
---|---|---
`access` | Yes |  [`'private'` or `'public'`](https://vercel.com/docs/vercel-blob#private-and-public-storage). Determines the access level of the blob.
`contentType` | No | The `application/octet-stream` when no extension exists or can't be matched.
`token` | No | A string specifying the token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](https://vercel.com/docs/vercel-blob/using-blob-sdk#read-write-token). You can also pass a client token created with the `generateClientTokenFromReadWriteToken` method
`addRandomSuffix` | No | A boolean specifying whether to add a random suffix to the pathname. It defaults to `true`.
`cacheControlMaxAge` | No | A number in seconds to configure the edge and browser cache. Defaults to one month. See the [caching](https://vercel.com/docs/storage/vercel-blob#caching) documentation for more details.
`abortSignal` | No | An
`createMultipartUpload()` returns a `JSON` object with the following data for the created upload:
```
{
  "key": "string",
  "uploadId": "string"
}
```

Phase 2: Upload all the parts
In the multipart uploader process, it's necessary for you to manage both memory usage and concurrent upload requests. Additionally, each part must be a minimum of 5MB, except the last one which can be smaller, and all parts should be of equal size.
TypeScriptPython
```
const part = await uploadPart(pathname, chunkBody, options);
```

```
from vercel.blob import upload_part

chunk1 = file_data[0:5*1024*1024] # minimum 5MB each, except last part
part = upload_part(
    "videos/intro.mp4",
    chunk1,
    access="private",  # or "public",
    upload_id=multipart_upload.upload_id,
    key=multipart_upload.key,
    part_number=1,
)
```

`uploadPart` accepts the following parameters:
  * `pathname`: (Required) Same value as the `pathname` parameter passed to `createMultipartUpload`
  * `chunkBody`: (Required) A blob object as `ReadableStream`, `String`, `ArrayBuffer` or `Blob` based on these
  * `options`: (Required) A `JSON` object with the following required and optional parameters:


Parameter | Required | Values
---|---|---
`access` | Yes |  [`'private'` or `'public'`](https://vercel.com/docs/vercel-blob#private-and-public-storage). Determines the access level of the blob.
`partNumber` | Yes | A number identifying which part is uploaded
`key` | Yes | A string returned from `createMultipartUpload` which identifies the blob object
`uploadId` | Yes | A string returned from `createMultipartUpload` which identifies the multipart upload
`token` | No | A string specifying the token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](https://vercel.com/docs/vercel-blob/using-blob-sdk#read-write-token). You can also pass a client token created with the `generateClientTokenFromReadWriteToken` method
`abortSignal` | No | An
`uploadPart()` returns a `JSON` object with the following data for the uploaded part:
```
{
  "etag": "string",
  "partNumber": "number"
}
```

Phase 3: Complete the multipart upload
TypeScriptPython
```
const blob = await completeMultipartUpload(pathname, parts, options);
```

```
from vercel.blob import complete_multipart_upload

blob = complete_multipart_upload(
    "videos/intro.mp4",
    [part1, part2, part3],
    access="private",  # or "public",
    upload_id=multipart_upload.upload_id,
    key=multipart_upload.key,
)
```

`completeMultipartUpload` accepts the following parameters:
  * `pathname`: (Required) Same value as the `pathname` parameter passed to `createMultipartUpload`
  * `parts`: (Required) An array containing all the uploaded parts
  * `options`: (Required) A `JSON` object with the following required and optional parameters:


Parameter | Required | Values
---|---|---
`access` | Yes |  [`'private'` or `'public'`](https://vercel.com/docs/vercel-blob#private-and-public-storage). Determines the access level of the blob.
`key` | Yes | A string returned from `createMultipartUpload` which identifies the blob object
`uploadId` | Yes | A string returned from `createMultipartUpload` which identifies the multipart upload
`contentType` | No | The `application/octet-stream` when no extension exists or can't be matched.
`token` | No | A string specifying the token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](https://vercel.com/docs/vercel-blob/using-blob-sdk#read-write-token). You can also pass a client token created with the `generateClientTokenFromReadWriteToken` method
`addRandomSuffix` | No | A boolean specifying whether to add a random suffix to the pathname. It defaults to `true`.
`cacheControlMaxAge` | No | A number in seconds to configure the edge and browser cache. Defaults to one month. See the [caching](https://vercel.com/docs/storage/vercel-blob#caching) documentation for more details.
`abortSignal` | No | An
`completeMultipartUpload()` returns a `JSON` object with the following data for the created blob object:
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

###  [Uploader](https://vercel.com/docs/vercel-blob/using-blob-sdk#uploader)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#uploader)
A less verbose way than the manual process is the multipart uploader method. It's a wrapper around the manual multipart upload process and takes care of the data that is the same for all the three multipart phases. This results in a simpler API, but still requires you to handle memory usage and concurrent upload requests.
Phase 1: Create the multipart uploader
TypeScriptPython
```
const uploader = await createMultipartUploader(pathname, options);
```

```
from vercel.blob import AsyncBlobClient

client = AsyncBlobClient()
uploader = await client.create_multipart_uploader(
    "examples/large-file.bin",
    content_type="application/octet-stream",
    add_random_suffix=True,
)
```

`createMultipartUploader` accepts the following parameters:
  * `pathname`: (Required) A string specifying the path inside the blob store. This will be the base value of the return URL and includes the filename and extension.
  * `options`: (Required) A `JSON` object with the following required and optional parameters:


Parameter | Required | Values
---|---|---
`access` | Yes |  [`'private'` or `'public'`](https://vercel.com/docs/vercel-blob#private-and-public-storage). Determines the access level of the blob.
`contentType` | No | The `application/octet-stream` when no extension exists or can't be matched.
`token` | No | A string specifying the token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](https://vercel.com/docs/vercel-blob/using-blob-sdk#read-write-token). You can also pass a client token created with the `generateClientTokenFromReadWriteToken` method
`addRandomSuffix` | No | A boolean specifying whether to add a random suffix to the pathname. It defaults to `true`.
`cacheControlMaxAge` | No | A number in seconds to configure the edge and browser cache. Defaults to one month. See the [caching](https://vercel.com/docs/storage/vercel-blob#caching) documentation for more details.
`abortSignal` | No | An
`createMultipartUploader()` returns an `Uploader` object with the following attributes and methods:
TypeScriptPython
```
{
  key: string;
  uploadId: string;
  uploadPart: (partNumber: number, body: BodyInit) => Promise<Part>;
  complete: (parts: Part[]) => Promise<PutBlobResult>;
}
```

```
uploader.upload_id                              # string
uploader.key                                    # string
uploader.upload_part(part_number, chunk_body)   # method
uploader.complete(parts)                        # method
```

Phase 2: Upload all the parts
In the multipart uploader process, it's necessary for you to manage both memory usage and concurrent upload requests. Additionally, each part must be a minimum of 5MB, except the last one which can be smaller, and all parts should be of equal size.
TypeScriptPython
```
const part1 = await uploader.uploadPart(1, chunkBody1);
const part2 = await uploader.uploadPart(2, chunkBody2);
const part3 = await uploader.uploadPart(3, chunkBody3);
```

```
import asyncio
tasks = [
    uploader.upload_part(1, chunk_body_1),
    uploader.upload_part(2, chunk_body_2),
    uploader.upload_part(3, chunk_body_3),
]
parts = await asyncio.gather(*tasks)
```

`uploader.uploadPart` accepts the following parameters:
  * `partNumber`: (Required) A number identifying which part is uploaded
  * `chunkBody`: (Required) A blob object as `ReadableStream`, `String`, `ArrayBuffer` or `Blob` based on these


`uploader.uploadPart()` returns an object with the following data for the uploaded part:
TypeScriptPython
```
{
  etag: string;
  partNumber: number;
}
```

```
part.etag         # string
part.part_number  # int
```

Phase 3: Complete the multipart upload
TypeScriptPython
```
const blob = await uploader.complete([part1, part2, part3]);
```

```
blob = await uploader.complete([part_1, part_2, part_3])
```

`uploader.complete` accepts the following parameters:
  * `parts`: (Required) An array containing all the uploaded parts


`uploader.complete()` returns an object with the following data for the created blob object:
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
result.pathname             # string
result.content_type         # string
result.content_disposition  # string
result.url                  # string
result.download_url         # string
result.etag                 # string
```
