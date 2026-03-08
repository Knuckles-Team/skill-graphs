Menu
Menu
# NEXTJS_NO_FETCH_IN_SERVER_PROPS
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Since both `getServerSideProps` and API routes run on the server, calling `fetch` on a non-relative URL will trigger an additional network request.
##  [How to fix](https://vercel.com/docs/conformance/rules/NEXTJS_NO_FETCH_IN_SERVER_PROPS#how-to-fix)[](https://vercel.com/docs/conformance/rules/NEXTJS_NO_FETCH_IN_SERVER_PROPS#how-to-fix)
Instead of using `fetch` to make a call to the API route, you can instead share the code in a shared library or module to avoid another network request. You can then import this hared logic and call directly within your `getServerSideProps` function, avoiding additional network requests entirely.
* * *
Was this helpful?
Send
