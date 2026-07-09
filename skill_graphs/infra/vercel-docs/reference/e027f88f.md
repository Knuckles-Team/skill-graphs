# NO_INLINE_SVG
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule is available from version 1.3.0.
Preventing the use of `<svg></svg>` inline improves the health of your codebase at the page level. Using inlined `svg` tags in excess can cause hydration issues, negatively impact the performance of both the browser and the server rendering.
By default, this rule is disabled. To enable it, refer to [customizing Conformance](https://vercel.com/docs/conformance/customize).
