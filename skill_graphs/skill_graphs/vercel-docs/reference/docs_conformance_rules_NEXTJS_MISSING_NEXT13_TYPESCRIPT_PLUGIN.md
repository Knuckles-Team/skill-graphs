Menu
Menu
# NEXTJS_MISSING_NEXT13_TYPESCRIPT_PLUGIN
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Next 13 introduced a TypeScript plugin to provide richer information for Next.js applications using TypeScript. See the
##  [How to fix](https://vercel.com/docs/conformance/rules/NEXTJS_MISSING_NEXT13_TYPESCRIPT_PLUGIN#how-to-fix)[](https://vercel.com/docs/conformance/rules/NEXTJS_MISSING_NEXT13_TYPESCRIPT_PLUGIN#how-to-fix)
Add the following to `plugins` in the `compilerOptions` of your `tsconfig.json` file.
tsconfig.json
```
  "compilerOptions": {
    "plugins": [{ "name": "next" }]
  }
```

* * *
Was this helpful?
Send
