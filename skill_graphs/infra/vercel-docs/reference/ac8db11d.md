##  [Creating a public Blob store](https://vercel.com/docs/vercel-blob/public-storage#creating-a-public-blob-store)[](https://vercel.com/docs/vercel-blob/public-storage#creating-a-public-blob-store)
You can create a public Blob store from the Vercel dashboard or the CLI:
  * Dashboard:
    1. Go to your project's [Storage tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fstores&title=Go+to+Storage)
    2. Select Create Database, then choose Blob
    3. Select Continue, then set the access to Public
  * [CLI](https://vercel.com/docs/cli/blob): Run `vercel blob create-store [name] --access public`


Your project needs a `BLOB_READ_WRITE_TOKEN` environment variable to interact with the store. When you create a Blob store from a project, this variable is added automatically. When you create a store from the team level, you'll need to [connect it to a project](https://vercel.com/docs/storage#connecting-a-store-to-a-project) for the environment variable to be added.
