# NO_INSTANCEOF_ERROR
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule is available from version 1.5.0.
A common pattern for checking if an object is an error is to use `error instanceof Error`.
This pattern is problematic because errors can come from other `Error` constructor, and are therefore not instances of the current realm's global `Error` constructor and will not pass the `instanceof` check.
Some examples of where you might hit this include:
  * In Node.js, errors from a workers are instances of `Error` from the worker's global environment.
  * In browser environments, errors from `iframe` are instances of `Error` from the `iframe`'s global environment (i.e. `iframe.contentWindow.Error`).


By default, this rule is disabled. To enable it, refer to [customizing Conformance](https://vercel.com/docs/conformance/customize).
