##  [Multipart uploads](https://vercel.com/docs/vercel-blob#multipart-uploads)[](https://vercel.com/docs/vercel-blob#multipart-uploads)
Vercel Blob supports [multipart uploads](https://vercel.com/docs/vercel-blob/using-blob-sdk#multipart-uploads) for large files, which provides significant advantages when transferring substantial amounts of data.
Multipart uploads work by splitting large files into smaller chunks (parts) that are uploaded independently and then reassembled on the server. This approach offers several key benefits:
  * Improved upload reliability: If a network issue occurs during upload, only the affected part needs to be retried instead of restarting the entire upload
  * Better performance: Multiple parts can be uploaded in parallel, significantly increasing transfer speed
  * Progress tracking: More granular upload progress reporting as each part completes


We recommend using multipart uploads for files larger than 100 MB. Both the [`put()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#put) and [`upload()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#upload) methods handle all the complexity of splitting, uploading, and reassembling the file for you.
For billing purposes, multipart uploads count as multiple advanced operations:
  * One operation when starting the upload
  * One operation for each part uploaded
  * One operation for completing the upload


This approach ensures reliable handling of large files while maintaining the performance and efficiency expected from modern cloud storage solutions.
