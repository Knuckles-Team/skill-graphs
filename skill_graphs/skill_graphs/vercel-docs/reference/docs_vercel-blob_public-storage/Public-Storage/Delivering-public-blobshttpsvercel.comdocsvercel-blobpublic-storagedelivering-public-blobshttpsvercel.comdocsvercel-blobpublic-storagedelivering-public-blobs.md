##  [Delivering public blobs](https://vercel.com/docs/vercel-blob/public-storage#delivering-public-blobs)[](https://vercel.com/docs/vercel-blob/public-storage#delivering-public-blobs)
Every file uploaded to a public Blob store gets a URL in the form of `https://<store-id>.public.blob.vercel-storage.com/<pathname>`. You can use this URL directly in your HTML:
###  [Displaying an image](https://vercel.com/docs/vercel-blob/public-storage#displaying-an-image)[](https://vercel.com/docs/vercel-blob/public-storage#displaying-an-image)
```
<img
  src="https://my-store-id.public.blob.vercel-storage.com/avatar.png"
  alt="User avatar"
/>
```

To use `next.config.js`:
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      new URL('https://my-store-id.public.blob.vercel-storage.com/**'),
    ],
  },
};

module.exports = nextConfig;
```

Then use `Image` instead of `img`:
```
import Image from 'next/image';

<Image
  src="https://my-store-id.public.blob.vercel-storage.com/avatar.png"
  alt="User avatar"
  width={200}
  height={200}
/>
```

`next/image` with direct blob URLs only works with public Blob stores. For private blobs, serve files through your [Functions](https://vercel.com/docs/functions) using [`get()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#get) and use the function route URL as the image source.
###  [Linking a file for download](https://vercel.com/docs/vercel-blob/public-storage#linking-a-file-for-download)[](https://vercel.com/docs/vercel-blob/public-storage#linking-a-file-for-download)
```
<a href="https://my-store-id.public.blob.vercel-storage.com/report.pdf?download=1">
  Download report
</a>
```

Adding `?download=1` to a blob URL forces a file download, regardless of file type. The SDK also exposes this as the `downloadUrl` property on blob objects. Without it, the URL displays the file in the browser when the MIME type supports it (images, videos, audio, PDFs, plain text, XML, and JSON). All other MIME types automatically trigger a download.
This behavior is controlled by the `content-disposition` header. Vercel Blob sets it to `inline` for displayable types and `attachment` for everything else. This also prevents hosting HTML pages on Vercel Blob.
