##  [Setup Remote Caching for Turborepo on Vercel](https://vercel.com/docs/deployment-retention#setup-remote-caching-for-turborepo-on-vercel)[](https://vercel.com/docs/deployment-retention#setup-remote-caching-for-turborepo-on-vercel)
You can optionally choose to connect your Turborepo to the [Vercel Remote Cache](https://vercel.com/docs/monorepos/remote-caching) from your local machine, allowing you to share artifacts and completed computations with your team and CI/CD pipelines.
You do not need to host your project on Vercel to use Vercel Remote Caching. For more information, see the [Remote Caching](https://vercel.com/docs/monorepos/remote-caching) doc. You can also use a custom remote cache. For more information, see the
  1. ###  [Link your project to the Vercel Remote Cache](https://vercel.com/docs/deployment-retention#link-your-project-to-the-vercel-remote-cache)[](https://vercel.com/docs/deployment-retention#link-your-project-to-the-vercel-remote-cache)
First, authenticate with the Turborepo CLI from the root of your monorepo:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm dlx turbo login
```

```
yarn dlx turbo login
```

```
npx turbo login
```

```
bunx turbo login
```

Then, use [remote cache](https://vercel.com/docs/monorepos/remote-caching#link-to-the-remote-cache). This command should be run from the root of your monorepo:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm dlx turbo link
```

```
yarn dlx turbo link
```

```
npx turbo link
```

```
bunx turbo link
```

Next, `cd` into each project in your Turborepo and run `vercel link` to link each directory within the monorepo to your Vercel Project.
As a Team owner, you can also [enable caching within the Vercel Dashboard](https://vercel.com/docs/monorepos/remote-caching#enable-and-disable-remote-caching-for-your-team).
  2. ###  [Test the caching](https://vercel.com/docs/deployment-retention#test-the-caching)[](https://vercel.com/docs/deployment-retention#test-the-caching)
Your project now has the Remote Cache linked. Run `turbo run build` to see the caching in action. Turborepo caches the filesystem output both locally and remote (cloud). To see the cached artifacts open `node_modules/.cache/turbo`.
Now try making a change in a file and running `turbo run build` again. The build speed will have dramatically improved. This is because Turborepo will only rebuild the changed files.
To see information about the [Remote Cache usage](https://vercel.com/docs/limits/usage#artifacts), go to the Artifacts section of the Usage section in the sidebar.
