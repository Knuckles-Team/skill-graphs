##  [How to fix](https://vercel.com/docs/conformance/rules/NO_FETCH_FROM_MIDDLEWARE#how-to-fix)[](https://vercel.com/docs/conformance/rules/NO_FETCH_FROM_MIDDLEWARE#how-to-fix)
The correct fix will depend on the specific situation. If the server that is being called is globally distributed, then this asynchronous call may be okay. If not, then the code should try to remove the `fetch` statement to avoid making a request that would add latency to middleware.
* * *
Was this helpful?
Send
On this page
  * [Example](https://vercel.com/docs/conformance/rules/NO_FETCH_FROM_MIDDLEWARE#example)
  * [How to fix](https://vercel.com/docs/conformance/rules/NO_FETCH_FROM_MIDDLEWARE#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
