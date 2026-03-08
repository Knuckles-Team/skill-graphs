##  [Using Vercel Blob in your workflow](https://vercel.com/docs/vercel-blob#using-vercel-blob-in-your-workflow)[](https://vercel.com/docs/vercel-blob#using-vercel-blob-in-your-workflow)
If you'd like to know whether or not Vercel Blob can be integrated into your workflow, it's worth knowing the following:
  * You can have one or more Vercel Blob stores per Vercel account
  * You can use multiple Vercel Blob stores in one Vercel project
  * Each Vercel Blob store can be accessed by multiple Vercel projects
  * Read access:
    * With private Blob stores: all read access requires authentication
    * With public Blob stores: blob URLs are accessible to anyone with the link
  * To add to or remove from the content of a Blob store, a valid [token](https://vercel.com/docs/storage/vercel-blob/using-blob-sdk#read-write-token) is required


###  [Transferring to another project](https://vercel.com/docs/vercel-blob#transferring-to-another-project)[](https://vercel.com/docs/vercel-blob#transferring-to-another-project)
If you need to transfer your blob store from one project to another project in the same or different team, review [Transferring your store](https://vercel.com/docs/storage#transferring-your-store).
