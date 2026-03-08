##  [Private and public storage](https://vercel.com/docs/vercel-blob#private-and-public-storage)[](https://vercel.com/docs/vercel-blob#private-and-public-storage)
Files are private or public depending on the store you create. The access mode defines how files are accessed and delivered. Use the following table to understand the differences between the two modes:
| Private storage | Public storage
---|---|---
Write access | Authenticated | Authenticated
Read access | Authenticated (token required) | Anyone with the URL
Delivery | Through your [Functions](https://vercel.com/docs/functions) via [`get()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#get) | Direct blob URL
Best for | Sensitive documents, user content, custom auth | Large media, images, videos, public assets
It's important to choose the correct access mode for your use case since you cannot change it after the creation of a blob store.
Learn more about [private storage](https://vercel.com/docs/vercel-blob/private-storage) and [public storage](https://vercel.com/docs/vercel-blob/public-storage).
