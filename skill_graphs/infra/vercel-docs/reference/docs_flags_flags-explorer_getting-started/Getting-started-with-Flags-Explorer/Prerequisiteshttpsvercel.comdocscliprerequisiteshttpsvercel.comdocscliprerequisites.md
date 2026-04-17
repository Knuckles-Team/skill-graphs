##  [Prerequisites](https://vercel.com/docs/cli#prerequisites)[](https://vercel.com/docs/cli#prerequisites)
  * Set up the [Vercel Toolbar](https://vercel.com/docs/vercel-toolbar) for development by following [adding the Vercel Toolbar to local and production environments](https://vercel.com/docs/vercel-toolbar/in-production-and-localhost)
  * You should have the latest version of Vercel CLI installed. To check your version, use `vercel --version`. To [install](https://vercel.com/docs/cli#installing-vercel-cli) or update Vercel CLI, use:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i -g vercel@latest
```

```
yarn global add vercel@latest
```

```
npm i -g vercel@latest
```

```
bun add -g vercel@latest
```

  * Ensure your local directory [links](https://vercel.com/docs/cli/link) to a Vercel project. You can use `vercel link` from root of your project to link it to your Vercel account or use:
Terminal
```
vercel link [path-to-directory]
```
