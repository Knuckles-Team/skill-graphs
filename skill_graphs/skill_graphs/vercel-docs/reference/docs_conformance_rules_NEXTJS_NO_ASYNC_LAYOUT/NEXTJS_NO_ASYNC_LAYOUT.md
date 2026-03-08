# NEXTJS_NO_ASYNC_LAYOUT
Last updated June 27, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule is in preview, please give us your feedback!


This rule is available from version 1.1.0.
This rule examines all Next.js app router layout files and their transitive dependencies to ensure none are asynchronous or return new Promise instances. Even if the layout component itself is not asynchronous, importing an asynchronous component somewhere in the layout's dependency tree can silently cause the layout to render dynamically. This can cause a blank layout to be displayed to the user while Next.js waits for long promises to resolve.
By default, this rule is disabled. To enable it, refer to [customizing Conformance](https://vercel.com/docs/conformance/customize).
For further reading, these resources may be helpful:
  * `dynamic` export and how it can be used to force the dynamic behavior of a layout.
