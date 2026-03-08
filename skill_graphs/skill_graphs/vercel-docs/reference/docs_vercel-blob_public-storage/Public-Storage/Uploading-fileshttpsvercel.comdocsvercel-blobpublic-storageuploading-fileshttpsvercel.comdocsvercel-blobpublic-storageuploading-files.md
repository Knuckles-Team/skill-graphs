##  [Uploading files](https://vercel.com/docs/vercel-blob/public-storage#uploading-files)[](https://vercel.com/docs/vercel-blob/public-storage#uploading-files)
Upload files to a public Blob store using [`put()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#put) with `access: 'public'`:
app/api/upload/route.ts
```
import { put } from '@vercel/blob';

export async function POST(request: Request) {
  const form = await request.formData();
  const file = form.get('file') as File;

  const blob = await put(file.name, file, {
    access: 'public',
  });

  return Response.json(blob);
}
```

See the [server uploads](https://vercel.com/docs/storage/vercel-blob/server-upload) and [client uploads](https://vercel.com/docs/storage/vercel-blob/client-upload) guides for detailed instructions on uploading files.
