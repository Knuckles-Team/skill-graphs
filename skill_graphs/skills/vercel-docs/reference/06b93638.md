##  [Getting started](https://vercel.com/docs/vercel-blob#getting-started)[](https://vercel.com/docs/vercel-blob#getting-started)
```
import { put } from '@vercel/blob';

const blob = await put('avatar.jpg', imageFile, {
  access: 'private' /* or 'public' */
});
```

You can create and manage your Vercel Blob stores from your [account dashboard](https://vercel.com/dashboard) or the [Vercel CLI](https://vercel.com/docs/cli/blob). You can create blob stores in any of the 20 [regions](https://vercel.com/docs/regions#region-list) to optimize performance and meet data residency requirements. You can scope your Vercel Blob stores to your Hobby team or [team](https://vercel.com/docs/accounts/create-a-team), and connect them to as many projects as you want.
To get started, see the [server-side](https://vercel.com/docs/storage/vercel-blob/server-upload), or [client-side](https://vercel.com/docs/storage/vercel-blob/client-upload) quickstart guides. Or visit the full API reference for the [Vercel Blob SDK](https://vercel.com/docs/storage/vercel-blob/using-blob-sdk).
