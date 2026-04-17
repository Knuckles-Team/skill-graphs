# PACKAGE_JSON_PRIVATE_REQUIREDPACKAGE_JSON_SIDE_EFFECTS_REQUIRED
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This check ensures that every `package.json` has a `sideEffects` field. The `sideEffects` field is required for shared packages. This field helps bundlers make assumptions about packages that improve tree shaking, or pruning files that aren't used and don't have any global side effects.
See
