##  [How To Fix](https://vercel.com/docs/conformance/rules/ESLINT_NEXT_RULES_REQUIRED#how-to-fix)[](https://vercel.com/docs/conformance/rules/ESLINT_NEXT_RULES_REQUIRED#how-to-fix)
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
Was this helpful?
Send
On this page
  * [Example](https://vercel.com/docs/conformance/rules/ESLINT_NEXT_RULES_REQUIRED#example)
  * [How To Fix](https://vercel.com/docs/conformance/rules/ESLINT_NEXT_RULES_REQUIRED#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
