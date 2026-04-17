# NEXTJS_SAFE_NEXT_PUBLIC_ENV_USAGE
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule is available from version 1.4.0.
The use of `process.env.NEXT_PUBLIC_*` environment variables may warrant a review from other developers to ensure there are no unintended leakage of environment variables.
When enabled, this rule requires that all usage of `NEXT_PUBLIC_*` must be included in the [allowlist](https://vercel.com/docs/conformance/allowlist).
