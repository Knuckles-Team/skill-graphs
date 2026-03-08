##  [Setup Remote Caching for Nx on Vercel](https://vercel.com/docs/monorepos/nx#setup-remote-caching-for-nx-on-vercel)[](https://vercel.com/docs/monorepos/nx#setup-remote-caching-for-nx-on-vercel)
Before using remote caching with Nx, do one of the following:
  * Ensure the `NX_CACHE_DIRECTORY=/tmp/nx-cache` is set


or
  * Set the `cacheDirectory` option to `/tmp/nx-cache` at `tasksRunnerOptions.{runner}.options` in your `nx.json`. For example:


nx.json
```
"tasksRunnerOptions": {
  "default": {
    "runner": "nx/tasks-runners/default",
    "options": {
      "cacheDirectory": "/tmp/nx-cache"
    }
  }
}
```

To configure Remote Caching for your Nx project on Vercel, use the
  1. ###  [Install the `@vercel/remote-nx` plugin](https://vercel.com/docs/monorepos/nx#install-the-@vercel/remote-nx-plugin)[](https://vercel.com/docs/monorepos/nx#install-the-@vercel/remote-nx-plugin)
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @vercel/remote-nx
```

```
yarn add @vercel/remote-nx
```

```
npm i @vercel/remote-nx
```

```
bun add @vercel/remote-nx
```

  2. ###  [Configure the `@vercel/remote-nx` runner](https://vercel.com/docs/monorepos/nx#configure-the-@vercel/remote-nx-runner)[](https://vercel.com/docs/monorepos/nx#configure-the-@vercel/remote-nx-runner)
In your `nx.json` file you will find a `tasksRunnerOptions` field. Update this field so that it's using the installed `@vercel/remote-nx`:
nx.json
```
{
  "tasksRunnerOptions": {
    "default": {
      "runner": "@vercel/remote-nx",
      "options": {
        "cacheableOperations": ["build", "test", "lint", "e2e"],
        "token": "<token>",
        "teamId": "<teamId>"
      }
    }
  }
}
```

You can specify your `token` and `teamId` in your nx.json or set them as environment variables.
Parameter | Description | Environment Variable / .env | `nx.json`
---|---|---|---
Vercel Access Token | Vercel access token with access to the provided team | `NX_VERCEL_REMOTE_CACHE_TOKEN` | `token`
Vercel [Team ID](https://vercel.com/docs/accounts#find-your-team-id) (optional) | The Vercel Team ID that should share the Remote Cache | `NX_VERCEL_REMOTE_CACHE_TEAM` | `teamId`
When deploying on Vercel, these variables will be automatically set for you.
  3. ###  [Clear cache and run](https://vercel.com/docs/monorepos/nx#clear-cache-and-run)[](https://vercel.com/docs/monorepos/nx#clear-cache-and-run)
Clear your local cache and rebuild your project.
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm dlx nx reset
```

```
yarn dlx nx reset
```

```
npx nx reset
```

```
bunx nx reset
```

Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm dlx nx build
```

```
yarn dlx nx build
```

```
npx nx build
```

```
bunx nx build
```



* * *
[ Previous Remote Caching ](https://vercel.com/docs/monorepos/remote-caching)[ Next Monorepos FAQ ](https://vercel.com/docs/monorepos/monorepo-faq)
Was this helpful?
Send
On this page
  * [Deploy Nx to Vercel](https://vercel.com/docs/monorepos/nx#deploy-nx-to-vercel)
  * [Ensure your Nx project is configured correctly](https://vercel.com/docs/monorepos/nx#ensure-your-nx-project-is-configured-correctly)
  * [Import your project](https://vercel.com/docs/monorepos/nx#import-your-project)
  * [Next steps](https://vercel.com/docs/monorepos/nx#next-steps)
  * [Using nx-ignore](https://vercel.com/docs/monorepos/nx#using-nx-ignore)
  * [Setup Remote Caching for Nx on Vercel](https://vercel.com/docs/monorepos/nx#setup-remote-caching-for-nx-on-vercel)
  * [Install the @vercel/remote-nx plugin](https://vercel.com/docs/monorepos/nx#install-the-@vercel/remote-nx-plugin)
  * [Configure the @vercel/remote-nx runner](https://vercel.com/docs/monorepos/nx#configure-the-@vercel/remote-nx-runner)
  * [Clear cache and run](https://vercel.com/docs/monorepos/nx#clear-cache-and-run)


Copy as MarkdownGive feedbackAsk AI about this page
