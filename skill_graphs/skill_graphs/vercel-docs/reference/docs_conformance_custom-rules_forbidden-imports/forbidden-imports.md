# forbidden-imports
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
The `forbidden-imports` rule type enables you to disallow one or more files from importing one or more predefined modules.
Unlike [`forbidden-dependencies`](https://vercel.com/docs/conformance/custom-rules/forbidden-dependencies), this rule type won't check for indirect (transitive) dependencies. This makes this rule faster, but limits its effectiveness.
