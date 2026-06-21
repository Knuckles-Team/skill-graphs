##  [How to fix](https://vercel.com/docs/conformance/rules/NEXTJS_SAFE_URL_IMPORTS#how-to-fix)[](https://vercel.com/docs/conformance/rules/NEXTJS_SAFE_URL_IMPORTS#how-to-fix)
Engineers should reach out to the appropriate engineer(s) or team(s) for a security review of the URL import configuration.
When requesting a review, please provide as much information as possible around the proposed URL being added, and if there any security implications for using the URL.
If this URL is deemed safe for general use, it can be added to the list of approved URL imports. This can be done by following the [Customizing Conformance](https://vercel.com/docs/conformance/customize#configuring-a-conformance-rule) docs to add the URL to your `conformance.config.jsonc` file:
conformance.config.jsonc
```
"NEXTJS_SAFE_URL_IMPORTS": {
  urlImports: [theUrlToAdd],
}
```

* * *
Was this helpful?
Send
On this page
  * [How to fix](https://vercel.com/docs/conformance/rules/NEXTJS_SAFE_URL_IMPORTS#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
