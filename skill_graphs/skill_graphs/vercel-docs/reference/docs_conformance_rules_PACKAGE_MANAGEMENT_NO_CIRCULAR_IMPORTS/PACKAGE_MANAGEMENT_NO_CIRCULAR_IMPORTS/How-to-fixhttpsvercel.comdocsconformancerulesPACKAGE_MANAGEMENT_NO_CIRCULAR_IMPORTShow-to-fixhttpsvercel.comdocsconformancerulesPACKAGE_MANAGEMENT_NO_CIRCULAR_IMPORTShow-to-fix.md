##  [How to fix](https://vercel.com/docs/conformance/rules/PACKAGE_MANAGEMENT_NO_CIRCULAR_IMPORTS#how-to-fix)[](https://vercel.com/docs/conformance/rules/PACKAGE_MANAGEMENT_NO_CIRCULAR_IMPORTS#how-to-fix)
The exports in the file that has a circular import should be refactored so that the circular import doesn't exist anymore. This might be fixed by moving some of the exports in a file to a separate file so that the imports don't cause a circular import. In some cases, it may be necessary to refactor the code to avoid the circular import.
* * *
Was this helpful?
Send
On this page
  * [Example](https://vercel.com/docs/conformance/rules/PACKAGE_MANAGEMENT_NO_CIRCULAR_IMPORTS#example)
  * [How to fix](https://vercel.com/docs/conformance/rules/PACKAGE_MANAGEMENT_NO_CIRCULAR_IMPORTS#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
