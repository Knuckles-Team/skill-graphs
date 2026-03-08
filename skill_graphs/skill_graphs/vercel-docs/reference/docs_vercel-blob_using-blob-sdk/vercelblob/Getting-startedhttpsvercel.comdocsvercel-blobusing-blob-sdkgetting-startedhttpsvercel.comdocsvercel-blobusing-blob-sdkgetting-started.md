##  [Getting started](https://vercel.com/docs/vercel-blob/using-blob-sdk#getting-started)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#getting-started)
To start using [Vercel Blob](https://vercel.com/storage/blob) SDK, follow the steps below:
You can also interact with Vercel Blob using the [Vercel CLI](https://vercel.com/docs/cli/blob) for command-line operations. For example, you might want to quickly upload assets during local development without writing additional code.
Vercel Blob works with any frontend framework. begin by installing the package:
TypeScriptPython
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @vercel/blob
```

```
yarn add @vercel/blob
```

```
npm i @vercel/blob
```

```
bun add @vercel/blob
```

```
pip install vercel
```

  1. ###  [Create a Blob store](https://vercel.com/docs/vercel-blob/using-blob-sdk#create-a-blob-store)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#create-a-blob-store)
    1. Go to your project's [Storage tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fstores&title=Go+to+Storage)
    2. Select Create Database, then choose Blob
    3. Select Continue, then set the access to Private or Public
    4. Choose a name for your store and select Create a new Blob store
    5. Select the environments where you would like the read-write token to be included. You can also update the prefix of the Environment Variable in Advanced Options
Once created, you are taken to the Vercel Blob store page.
  2. ###  [Prepare your local project](https://vercel.com/docs/vercel-blob/using-blob-sdk#prepare-your-local-project)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#prepare-your-local-project)
Since you created the Blob store in a project, environment variables are automatically created and added to the project for you.
     * `BLOB_READ_WRITE_TOKEN`
To use this environment variable locally, use the Vercel CLI to [pull the values into your local project](https://vercel.com/docs/cli/env#exporting-development-environment-variables):
```
vercel env pull
```
