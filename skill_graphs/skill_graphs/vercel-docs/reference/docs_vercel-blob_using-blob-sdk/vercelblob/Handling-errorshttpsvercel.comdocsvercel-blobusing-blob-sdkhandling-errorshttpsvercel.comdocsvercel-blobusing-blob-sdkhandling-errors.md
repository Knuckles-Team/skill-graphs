##  [Handling errors](https://vercel.com/docs/vercel-blob/using-blob-sdk#handling-errors)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#handling-errors)
When you make a request to the SDK using any of the above methods, they will return an error if the request fails due to any of the following reasons:
  * Missing required parameters
  * An invalid token or a token that does not have access to the Blob object
  * Suspended Blob store
  * Blob file or Blob store not found
  * Precondition failed (when using `ifMatch` for [conditional writes](https://vercel.com/docs/vercel-blob#conditional-writes) and the ETag doesn't match)
  * Unforeseen or unknown errors


To catch these errors, wrap your requests with a `try/catch` statement as shown below:
TypeScriptPython
```
import { put, BlobAccessError } from '@vercel/blob';

try {
  await put(...);
} catch (error) {
  if (error instanceof BlobAccessError) {
    // handle a recognized error
  } else {
    // throw the error again if it's unknown
  throw error;
  }
}

```

```
from vercel.blob import BlobClient
from vercel.blob.errors import BlobError, BlobNotFoundError

try:
    client = BlobClient()
    client.put(
        "examples/file.txt", b"hello",
        access="private",  # or "public"
    )
except BlobNotFoundError:
    # handle a recognized error
    ...
except BlobError as e:
    # handle other blob errors
    ...
except Exception as e:
    # handle unknown errors
    ...

```

* * *
[ Previous Client Uploads ](https://vercel.com/docs/vercel-blob/client-upload)[ Next Pricing ](https://vercel.com/docs/vercel-blob/usage-and-pricing)
Was this helpful?
Send
Next.js (/app)
Choose a framework to optimize documentation to:
  * Next.js (/app)
  * Next.js (/pages)
  * Other frameworks


On this page
  * [Getting started](https://vercel.com/docs/vercel-blob/using-blob-sdk#getting-started)
  * [Create a Blob store](https://vercel.com/docs/vercel-blob/using-blob-sdk#create-a-blob-store)
  * [Prepare your local project](https://vercel.com/docs/vercel-blob/using-blob-sdk#prepare-your-local-project)
  * [Read-write token](https://vercel.com/docs/vercel-blob/using-blob-sdk#read-write-token)
  * [The access parameter](https://vercel.com/docs/vercel-blob/using-blob-sdk#the-access-parameter)
  * [Using the SDK methods](https://vercel.com/docs/vercel-blob/using-blob-sdk#using-the-sdk-methods)
  * [Upload a blob](https://vercel.com/docs/vercel-blob/using-blob-sdk#upload-a-blob)
  * [put()](https://vercel.com/docs/vercel-blob/using-blob-sdk#put)
  * [Example code with folder output](https://vercel.com/docs/vercel-blob/using-blob-sdk#example-code-with-folder-output)
  * [Example responses](https://vercel.com/docs/vercel-blob/using-blob-sdk#example-responses)
  * [Get a blob](https://vercel.com/docs/vercel-blob/using-blob-sdk#get-a-blob)
  * [get()](https://vercel.com/docs/vercel-blob/using-blob-sdk#get)
  * [Example](https://vercel.com/docs/vercel-blob/using-blob-sdk#example)
  * [Deleting blobs](https://vercel.com/docs/vercel-blob/using-blob-sdk#deleting-blobs)
  * [del()](https://vercel.com/docs/vercel-blob/using-blob-sdk#del)
  * [Get blob metadata](https://vercel.com/docs/vercel-blob/using-blob-sdk#get-blob-metadata)
  * [head()](https://vercel.com/docs/vercel-blob/using-blob-sdk#head)
  * [List blobs](https://vercel.com/docs/vercel-blob/using-blob-sdk#list-blobs)
  * [list()](https://vercel.com/docs/vercel-blob/using-blob-sdk#list)
  * [Pagination](https://vercel.com/docs/vercel-blob/using-blob-sdk#pagination)
  * [Folders](https://vercel.com/docs/vercel-blob/using-blob-sdk#folders)
  * [Copy a blob](https://vercel.com/docs/vercel-blob/using-blob-sdk#copy-a-blob)
  * [copy()](https://vercel.com/docs/vercel-blob/using-blob-sdk#copy)
  * [Multipart Uploads](https://vercel.com/docs/vercel-blob/using-blob-sdk#multipart-uploads)
  * [Automatic](https://vercel.com/docs/vercel-blob/using-blob-sdk#automatic)
  * [Manual](https://vercel.com/docs/vercel-blob/using-blob-sdk#manual)
  * [Uploader](https://vercel.com/docs/vercel-blob/using-blob-sdk#uploader)
  * [Client uploads](https://vercel.com/docs/vercel-blob/using-blob-sdk#client-uploads)
  * [upload()](https://vercel.com/docs/vercel-blob/using-blob-sdk#upload)
  * [handleUpload()](https://vercel.com/docs/vercel-blob/using-blob-sdk#handleupload)
  * [onBeforeGenerateToken()](https://vercel.com/docs/vercel-blob/using-blob-sdk#onbeforegeneratetoken)
  * [onUploadCompleted()](https://vercel.com/docs/vercel-blob/using-blob-sdk#onuploadcompleted)
  * [Client uploads routes](https://vercel.com/docs/vercel-blob/using-blob-sdk#client-uploads-routes)
  * [Handling errors](https://vercel.com/docs/vercel-blob/using-blob-sdk#handling-errors)


Copy as MarkdownGive feedbackAsk AI about this page
