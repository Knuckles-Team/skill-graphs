##  [SEO and search engine indexing](https://vercel.com/docs/vercel-blob/public-storage#seo-and-search-engine-indexing)[](https://vercel.com/docs/vercel-blob/public-storage#seo-and-search-engine-indexing)
###  [Search engine visibility of blobs](https://vercel.com/docs/vercel-blob/public-storage#search-engine-visibility-of-blobs)[](https://vercel.com/docs/vercel-blob/public-storage#search-engine-visibility-of-blobs)
While Vercel Blob URLs can be designed to be unique and unguessable (when using `addRandomSuffix: true`), they can still be indexed by search engines under certain conditions:
  * If you link to blob URLs from public webpages
  * If you embed blob content (images, PDFs, etc.) in indexed content
  * If you share blob URLs publicly, even in contexts outside your application


By default, Vercel Blob does not provide a `robots.txt` file or other indexing controls. This means search engines like Google may discover and index your blob content if they find links to it.
###  [Preventing search engine indexing](https://vercel.com/docs/vercel-blob/public-storage#preventing-search-engine-indexing)[](https://vercel.com/docs/vercel-blob/public-storage#preventing-search-engine-indexing)
If you want to prevent search engines from indexing your blob content, you need to upload a `robots.txt` file directly to your blob store:
  1. Go to your [Storage page](https://vercel.com/d?to=%2F%5Bteam%5D%2F~%2Fstores&title=Go+to+Storage) and select your blob store
  2. Upload a `robots.txt` file to the root of your blob store with appropriate directives


Example `robots.txt` content to block all crawling of your blob store:
`User-agent: * Disallow: / `
###  [Removing already indexed blob content](https://vercel.com/docs/vercel-blob/public-storage#removing-already-indexed-blob-content)[](https://vercel.com/docs/vercel-blob/public-storage#removing-already-indexed-blob-content)
If your blob content has already been indexed by search engines:
  1. Verify your website ownership in
  2. Upload a `robots.txt` file to your blob store as described above
  3. Use the "Remove URLs" tool in Google Search Console to request removal
