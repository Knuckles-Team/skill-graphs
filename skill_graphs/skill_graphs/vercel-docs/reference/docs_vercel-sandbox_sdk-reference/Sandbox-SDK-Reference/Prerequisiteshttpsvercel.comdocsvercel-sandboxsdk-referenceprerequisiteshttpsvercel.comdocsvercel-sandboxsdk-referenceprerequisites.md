##  [Prerequisites](https://vercel.com/docs/vercel-sandbox/sdk-reference#prerequisites)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#prerequisites)
Install the SDK:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @vercel/sandbox
```

```
yarn add @vercel/sandbox
```

```
npm i @vercel/sandbox
```

```
bun add @vercel/sandbox
```

After installation:
  * Link your project and pull environment variables with `vercel link` and `vercel env pull` so the SDK can read a Vercel OpenID Connect (OIDC) token.
  * Choose a runtime: `node24`, `node22`, or `python3.13`.
