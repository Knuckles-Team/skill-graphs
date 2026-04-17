##  [Configuring Code Owners for Allowlists](https://vercel.com/docs/conformance/allowlist#configuring-code-owners-for-allowlists)[](https://vercel.com/docs/conformance/allowlist#configuring-code-owners-for-allowlists)
You can use [Code Owners](https://vercel.com/docs/code-owners) with allowlists for specific team reviews on updates. For instance, have the security team review security-related entries.
To configure Code Owners for all tests at the top level for the entire repository:
.vercel.approvers
```
**/*.allowlist.json @org/team:required
**/NO_CORS_HEADERS.* @org/security-team:required
```

For a specific workspace, add a `.vercel.approvers` file in the `.allowlists` sub-directory:
apps/docs/.allowlists/.vercel.approvers
```
NO_EXTERNAL_CSS_AT_IMPORTS.* @org/performance-team:required
```

The `:required` check ensures any modifications need the specified owners' review.
* * *
Was this helpful?
Send
On this page
  * [Anatomy of an allowlist entry](https://vercel.com/docs/conformance/allowlist#anatomy-of-an-allowlist-entry)
  * [The needsResolution field](https://vercel.com/docs/conformance/allowlist#the-needsresolution-field)
  * [Allowlists location](https://vercel.com/docs/conformance/allowlist#allowlists-location)
  * [Allowlisting all errors](https://vercel.com/docs/conformance/allowlist#allowlisting-all-errors)
  * [Configuring Code Owners for Allowlists](https://vercel.com/docs/conformance/allowlist#configuring-code-owners-for-allowlists)


Copy as MarkdownGive feedbackAsk AI about this page
