##  [How To Fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)[](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)
The recommended approach for configuring ESLint in a monorepo is to have a shared ESLint config in an internal package. See the
Once your monorepo has a shared ESLint config, you can add a `.eslintrc.cjs` file to the root folder of your workspace with the contents:
.eslintrc.cjs
```
module.exports = {
  root: true,
  extends: ['eslint-config-custom/base'],
};
```

You should also add `"eslint-config-custom": "workspace:*"` to your `devDependencies`.
* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [Example](https://vercel.com/docs/getting-started-with-vercel#example)
  * [How To Fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
