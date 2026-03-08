# Caching and Revalidating
Last updated February 27, 2026
Caching is a technique for storing the result of data fetching and other computations so that future requests for the same data can be served faster, without doing the work again. While revalidation allows you to update cache entries without having to rebuild your entire application.
Next.js provides a few APIs to handle caching and revalidation. This guide will walk you through when and how to use them.
  * [`fetch`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#fetch)
  * [`cacheTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#cachetag)
  * [`revalidateTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatetag)
  * [`updateTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#updatetag)
  * [`revalidatePath`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatepath)
  * [`unstable_cache`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#unstable_cache) (Legacy)
