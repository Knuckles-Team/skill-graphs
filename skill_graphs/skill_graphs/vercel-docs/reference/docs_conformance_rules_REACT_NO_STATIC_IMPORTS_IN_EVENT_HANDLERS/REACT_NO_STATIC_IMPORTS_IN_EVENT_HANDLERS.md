# REACT_NO_STATIC_IMPORTS_IN_EVENT_HANDLERS
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule has been deprecated as of version [1.8.0](https://vercel.com/docs/conformance/changelog#1.8.0)and will be removed in 2.0.0.
React event handlers are async, and as such, this means we can defer loading the associated code until we interact with the UI, triggering that event handler. Specifically, this means we can improve initial code size and the overhead of loading the code until it is actually needed.
