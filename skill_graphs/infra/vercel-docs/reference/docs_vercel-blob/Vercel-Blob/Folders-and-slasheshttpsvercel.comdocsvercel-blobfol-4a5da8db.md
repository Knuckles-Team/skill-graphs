##  [Folders and slashes](https://vercel.com/docs/vercel-blob#folders-and-slashes)[](https://vercel.com/docs/vercel-blob#folders-and-slashes)
Vercel Blob has folders support to organize your blobs:
```
const blob = await put('folder/file.txt', 'Hello World!', { access: 'private' /* or 'public' */ });
```

The path `folder/file.txt` creates a folder named `folder` and a blob named `file.txt`. To list all blobs within a folder, use the [`list`](https://vercel.com/docs/storage/vercel-blob/using-blob-sdk#list-blobs) function:
```
const listOfBlobs = await list({
  cursor,
  limit: 1000,
  prefix: 'folder/',
});
```

You don't need to create folders. Upload a file with a path containing a slash `/`, and Vercel Blob will interpret the slashes as folder delimiters.
In the Vercel Blob file browser on the Vercel dashboard, any pathname with a slash `/` is treated as a folder. However, these are not actual folders like in a traditional file system; they are used for organizing blobs in listings and the file browser.
