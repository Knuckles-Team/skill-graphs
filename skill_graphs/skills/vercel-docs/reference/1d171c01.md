# REACT_STABLE_CONTEXT_PROVIDER_VALUE
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
When non-stable values (i.e. object identities) are used as the `value` prop for `Context.Provider`, React will trigger cascading updates to all components that use this context value on each render, causing needless re-renders (affecting application performance) or causing unintended consequences that may negatively affect the user-experience.
