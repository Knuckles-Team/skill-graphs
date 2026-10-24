# NEXTJS_REQUIRE_EXPLICIT_DYNAMIC
Last updated September 24, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule is available from version 1.3.0.


This rule conflicts with the experimental Next.js feature [Partial Prerendering (PPR)](https://vercel.com/blog/partial-prerendering-with-next-js-creating-a-new-default-rendering-model). If you enable PPR in your Next.js app, you should not enable this rule.
For convenience, Next.js defaults to automatically selecting the rendering mode for pages and routes.
Whilst this works well, it also means that rendering modes can be changed unintentionally (i.e. through an update to a component that a page depends on). These changes can lead to unexpected behaviors, including performance issues.
To mitigate the chance that rendering modes change unexpectedly, you should explicitly set the `dynamic` route segment option to the desired mode. Note that the default value is `auto`, which will not satisfy this rule.
By default, this rule is disabled. To enable it, refer to [customizing Conformance](https://vercel.com/docs/conformance/customize).
For further reading, see:
