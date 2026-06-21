##  [Private and public storage delivery costs](https://vercel.com/docs/vercel-blob/usage-and-pricing#private-and-public-storage-delivery-costs)[](https://vercel.com/docs/vercel-blob/usage-and-pricing#private-and-public-storage-delivery-costs)
Private and public Blob stores are priced the same for storage, operations, and uploads. The difference is in how files are delivered, which affects data transfer costs.
Private blob delivery (e.g. a 10 KB document served through a [Function](https://vercel.com/docs/functions)):
  * Your Function fetches the blob from the store, then streams it to the browser
  * You pay [Blob Data Transfer](https://vercel.com/docs/vercel-blob#blob-data-transfer) + [Fast Origin Transfer](https://vercel.com/docs/pricing/networking#fast-origin-transfer) on cache miss for the Function-to-store fetch, plus [Fast Data Transfer](https://vercel.com/docs/cdn) + [Fast Origin Transfer](https://vercel.com/docs/pricing/networking#fast-origin-transfer) for the Function-to-browser response


Public blob delivery (e.g. a 150 KB image on a page):
  * The browser fetches the blob directly from the store
  * You pay [Blob Data Transfer](https://vercel.com/docs/vercel-blob#blob-data-transfer) + [Fast Origin Transfer](https://vercel.com/docs/pricing/networking#fast-origin-transfer) on cache miss
  * Blob Data Transfer (BDT) is 3x more cost-efficient than Fast Data Transfer (FDT) on average


For full details on how delivery works, see [delivering private blobs](https://vercel.com/docs/vercel-blob/private-storage#delivering-private-blobs) and [delivering public blobs](https://vercel.com/docs/vercel-blob/public-storage#delivering-public-blobs).
