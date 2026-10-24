##  [Customization](https://vercel.com/docs/conformance/rules/TYPESCRIPT_ONLY#customization)[](https://vercel.com/docs/conformance/rules/TYPESCRIPT_ONLY#customization)
The check supports custom file globs and ignore file globs that can be specified on `conformance.config.jsonc`. The globs take effect from the root of the workspace package.
conformance.config.jsonc
```
{
  "rules": {
    "TYPESCRIPT_ONLY": {
      "files": ["**/*.js", "**/*.jsx"],
      "ignoreFiles": ["**/*.custom-config.js"]
    }
  }
}
```

The default configuration is:
conformance.config.jsonc
```
{
  "rules": {
    "TYPESCRIPT_ONLY": {
      "files": ["**/*.{cjs,mjs,js,jsx}"],
      "ignoreFiles": [
        "dist/**",
        "node_modules/**",
        ".next/**", // Next.js output
        ".eslintrc.{cjs,js}", // Common ESLint config file name
        "*.config.{cjs,mjs,js}", // Common config file name
        "*.setup.{cjs,mjs,js}", // Common setup file name
      ],
    },
  },
}
```

* * *
Was this helpful?
Send
On this page
  * [Example](https://vercel.com/docs/conformance/rules/TYPESCRIPT_ONLY#example)
  * [How To Fix](https://vercel.com/docs/conformance/rules/TYPESCRIPT_ONLY#how-to-fix)
  * [Customization](https://vercel.com/docs/conformance/rules/TYPESCRIPT_ONLY#customization)


Copy as MarkdownGive feedbackAsk AI about this page
