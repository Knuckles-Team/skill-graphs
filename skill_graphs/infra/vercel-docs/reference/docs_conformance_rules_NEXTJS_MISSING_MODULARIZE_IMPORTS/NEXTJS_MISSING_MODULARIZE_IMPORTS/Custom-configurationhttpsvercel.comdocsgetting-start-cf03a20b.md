##  [Custom configuration](https://vercel.com/docs/getting-started-with-vercel#custom-configuration)[](https://vercel.com/docs/getting-started-with-vercel#custom-configuration)
You can also specify required `modularizeImports` config for your own packages.
In your `conformance.config.jsonc` file, add:
conformance.config.jsonc
```
NEXTJS_MISSING_MODULARIZE_IMPORTS: {
  requiredModularizeImports: [
    {
      moduleDependency: 'your-package-name',
      requiredConfig: {
        transform: 'your-package-name/{{member}}',
      },
    },
  ];
}
```

This will require that any workspace in your monorepo that uses the `your-package-name` package must use the provided `modularizeImports` config in their `next.config.js` file.
See [Customizing Conformance](https://vercel.com/docs/conformance/customize) for more information.
* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)
  * [Custom configuration](https://vercel.com/docs/getting-started-with-vercel#custom-configuration)


Copy as MarkdownGive feedbackAsk AI about this page
