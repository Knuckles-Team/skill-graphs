##  [How to fix](https://vercel.com/docs/conformance/rules/NEXTJS_NO_CLIENT_DEPS_IN_MIDDLEWARE#how-to-fix)[](https://vercel.com/docs/conformance/rules/NEXTJS_NO_CLIENT_DEPS_IN_MIDDLEWARE#how-to-fix)
Client dependencies used or transitively depended on by middleware files should be refactored to avoid depending on the client libraries. In the example above, the code that is used by middleware to fetch experiments should be moved to a separate file from the code that provides the React functionality.
* * *
Was this helpful?
Send
On this page
  * [Example](https://vercel.com/docs/conformance/rules/NEXTJS_NO_CLIENT_DEPS_IN_MIDDLEWARE#example)
  * [How to fix](https://vercel.com/docs/conformance/rules/NEXTJS_NO_CLIENT_DEPS_IN_MIDDLEWARE#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
