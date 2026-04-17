##  [How to fix](https://vercel.com/docs/conformance/rules/REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS#how-to-fix)[](https://vercel.com/docs/conformance/rules/REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS#how-to-fix)
To resolve this issue, add a JSDoc comment to the exported function.
```
/**
 * Modifies a string by appending `' world'` to it.
 */
export function appendWorld(str: string): string {
  return str + ' world';
}
```

You can add additional information to the JSDoc comment, such as descriptions of the function's parameters and return value.
```
/**
 * Modifies a string by appending `' world'` to it.
 *
 * @param str - The string to modify.
 * @returns The modified string.
 */
export function appendWorld(str: string): string {
  return str + ' world';
}
```

The example above doesn't provide type information in the JSDoc comment, as this information is already provided by the function signature. When working without TypeScript, you can also provide this information using JSDoc.
```
/**
 * Modifies a string by appending `' world'` to it.
 *
 * @param {string} str - The string to modify.
 * @returns {string} The modified string.
 */
export function appendWorld(str) {
  return str + ' world';
}
```

* * *
Was this helpful?
Send
On this page
  * [Examples](https://vercel.com/docs/conformance/rules/REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS#examples)
  * [How to fix](https://vercel.com/docs/conformance/rules/REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
