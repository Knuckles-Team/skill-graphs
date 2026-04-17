##  [Customization](https://vercel.com/docs/conformance/rules/TESTS_NO_ONLY#customization)[](https://vercel.com/docs/conformance/rules/TESTS_NO_ONLY#customization)
The default pattern matches the default patterns for Jest and Vitest, however you can provide your own patterns through the `paths` property.
The default configuration is:
conformance.config.jsonc
```
{
  "configuration": [
    "testPatterns": ["**/unit-tests/**/*.{js,jsx}"]
  ]
}
```

* * *
Was this helpful?
Send
On this page
  * [Example](https://vercel.com/docs/conformance/rules/TESTS_NO_ONLY#example)
  * [How to fix](https://vercel.com/docs/conformance/rules/TESTS_NO_ONLY#how-to-fix)
  * [Customization](https://vercel.com/docs/conformance/rules/TESTS_NO_ONLY#customization)


Copy as MarkdownGive feedbackAsk AI about this page
