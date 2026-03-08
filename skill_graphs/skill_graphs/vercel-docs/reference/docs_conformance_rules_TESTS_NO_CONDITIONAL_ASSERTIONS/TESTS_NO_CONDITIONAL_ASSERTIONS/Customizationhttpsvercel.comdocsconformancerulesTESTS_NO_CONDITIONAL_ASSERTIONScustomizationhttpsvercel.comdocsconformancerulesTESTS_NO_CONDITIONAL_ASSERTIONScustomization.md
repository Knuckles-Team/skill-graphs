##  [Customization](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#customization)[](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#customization)
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
  * [Example](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#example)
  * [How to fix](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#how-to-fix)
  * [Using expect.assertions](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#using-expect.assertions)
  * [What to do when you can't use expect.assertions](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#what-to-do-when-you-can't-use-expect.assertions)
  * [Customization](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#customization)


Copy as MarkdownGive feedbackAsk AI about this page
