##  [Client uploads](https://vercel.com/docs/vercel-blob/using-blob-sdk#client-uploads)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#client-uploads)
As seen in the [client uploads quickstart docs](https://vercel.com/docs/storage/vercel-blob/client-upload), you can upload files directly from clients (like browsers) to the Blob store.
All client uploads related methods are available under `@vercel/blob/client`.
###  [`upload()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#upload)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#upload)
The `upload` method is dedicated to [client uploads](https://vercel.com/docs/storage/vercel-blob/client-upload). It fetches a client token on your server using the `handleUploadUrl` before uploading the blob. Read the [client uploads](https://vercel.com/docs/storage/vercel-blob/client-upload) documentation to learn more.
```
upload(pathname, body, options);
```

It accepts the following parameters:
  * `pathname`: (Required) A string specifying the base value of the return URL
  * `body`: (Required) A blob object as `ReadableStream`, `String`, `ArrayBuffer` or `Blob` based on these
  * `options`: (Required) A `JSON` object with the following required and optional parameters:


Parameter | Required | Values
---|---|---
`access` | Yes |  [`'private'` or `'public'`](https://vercel.com/docs/vercel-blob#private-and-public-storage). Determines the access level of the blob.
`contentType` | No | A string indicating the
`handleUploadUrl` | Yes* | A string specifying the route to call for generating client tokens for [client uploads](https://vercel.com/docs/storage/vercel-blob/client-upload).
`clientPayload` | No | A string to be sent to your `handleUpload` server code. Example use-case: attaching the post id an image relates to. So you can use it to update your database.
`multipart` | No | Pass `multipart: true` when uploading large files. It will split the file into multiple parts, upload them in parallel and retry failed parts.
`abortSignal` | No | An
`onUploadProgress` | No | Callback to track upload progress: `onUploadProgress({loaded: number, total: number, percentage: number})`
`upload()` returns a `JSON` object with the following data for the created blob object:
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

An example `url` is:
`https://ce0rcu23vrrdzqap.public.blob.vercel-storage.com/profilesv1/user-12345-NoOVGDVcqSPc7VYCUAGnTzLTG2qEM2.txt `
###  [`handleUpload()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#handleupload)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#handleupload)
A server-side route helper to manage client uploads, it has two responsibilities:
  1. Generate tokens for client uploads
  2. Listen for completed client uploads, so you can update your database with the URL of the uploaded file for example


```
handleUpload(options);
```

It accepts the following parameters:
  * `options`: (Required) A `JSON` object with the following parameters:


Parameter | Required | Values
---|---|---
`token` | No | A string specifying the read-write token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](https://vercel.com/docs/vercel-blob/using-blob-sdk#read-write-token)
`request` | Yes | An `IncomingMessage` or `Request` object to be used to determine the action to take
[`onBeforeGenerateToken`](https://vercel.com/docs/vercel-blob/using-blob-sdk#onbeforegeneratetoken) | Yes | A function to be called right before generating client tokens for client uploads. See below for usage
[`onUploadCompleted`](https://vercel.com/docs/vercel-blob/using-blob-sdk#onuploadcompleted) | Yes | A function to be called by Vercel Blob when the client upload finishes. This is useful to update your database with the blob url that was uploaded
`body` | Yes | The request body
`handleUpload()` returns:
```
Promise<
  | { type: 'blob.generate-client-token'; clientToken: string }
  | { type: 'blob.upload-completed'; response: 'ok' }
>;
```

####  [`onBeforeGenerateToken()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#onbeforegeneratetoken)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#onbeforegeneratetoken)
The `onBeforeGenerateToken` function receives the following arguments:
  * `pathname`: The destination path for the blob
  * `clientPayload`: A string payload specified on the client when calling `upload()`
  * `multipart`: A boolean specifying whether the file is a multipart upload.


The function must return an object with the following properties:
Parameter | Required | Values
---|---|---
`addRandomSuffix` | No | A boolean specifying whether to add a random suffix to the `pathname`. It defaults to `false`. We recommend using this option to ensure there are no conflicts in your blob filenames.
`allowedContentTypes` | No | An array of strings specifying the `text/*`)
`maximumSizeInBytes` | No | A number specifying the maximum size in bytes that can be uploaded. The maximum is 5TB.
`validUntil` | No | A number specifying the timestamp in ms when the token will expire. By default, it's now + 1 hour.
`allowOverwrite` | No | A boolean to allow overwriting blobs. By default an error will be thrown if you try to overwrite a blob by using the same `pathname` for multiple blobs.
`cacheControlMaxAge` | No | A number in seconds to configure how long Blobs are cached. Defaults to one month. Cannot be set to a value lower than 1 minute. See the [caching](https://vercel.com/docs/storage/vercel-blob#caching) documentation for more details.
`callbackUrl` | No | A string specifying the URL that Vercel Blob will call when the upload completes. See [client uploads](https://vercel.com/docs/storage/vercel-blob/client-upload) for examples.
`tokenPayload` | No | A string specifying a payload to be sent to your server on upload completion.
####  [`onUploadCompleted()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#onuploadcompleted)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#onuploadcompleted)
The `onUploadCompleted` function receives the following arguments:
  * `blob`: The blob that was uploaded. See the return type of [`put()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#put) for more details.
  * `tokenPayload`: The payload that was defined in the [`onBeforeGenerateToken()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#onbeforegeneratetoken) function.


###  [Client uploads routes](https://vercel.com/docs/vercel-blob/using-blob-sdk#client-uploads-routes)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#client-uploads-routes)
Here's an example Next.js App Router route handler that uses `handleUpload()`:
app/api/post/upload/route.ts
```
import { handleUpload, type HandleUploadBody } from '@vercel/blob/client';
import { NextResponse } from 'next/server';

// Use-case: uploading images for blog posts
export async function POST(request: Request): Promise<NextResponse> {
  const body = (await request.json()) as HandleUploadBody;

  try {
    const jsonResponse = await handleUpload({
      body,
      request,
      onBeforeGenerateToken: async (pathname, clientPayload) => {
        // Generate a client token for the browser to upload the file
        // ⚠️ Authenticate and authorize users before generating the token.
        // Otherwise, you're allowing anonymous uploads.

        // ⚠️ When using the clientPayload feature, make sure to validate it
        // otherwise this could introduce security issues for your app
        // like allowing users to modify other users' posts

        return {
          allowedContentTypes: [
            // optional, default to all content types
            'image/jpeg',
            'image/png',
            'image/webp',
            'text/*',
          ],
          // callbackUrl: 'https://example.com/api/avatar/upload',
          // optional, `callbackUrl` is automatically computed when hosted on Vercel
        };
      },
      onUploadCompleted: async ({ blob, tokenPayload }) => {
        // Get notified of client upload completion
        // ⚠️ This will not work on `localhost` websites,
        // Use ngrok or similar to get the full upload flow

        console.log('blob upload completed', blob, tokenPayload);

        try {
          // Run any logic after the file upload completed,
          // If you've already validated the user and authorization prior, you can
          // safely update your database
        } catch (error) {
          throw new Error('Could not update post');
        }
      },
    });

    return NextResponse.json(jsonResponse);
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : String(error) },
      { status: 400 }, // The webhook will retry 5 times waiting for a 200
    );
  }
}
```
