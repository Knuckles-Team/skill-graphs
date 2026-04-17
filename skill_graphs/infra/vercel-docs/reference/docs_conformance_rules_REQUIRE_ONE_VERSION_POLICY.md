Menu
Menu
# REQUIRE_ONE_VERSION_POLICY
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Dependency mismatch is a common and easily preventable problem. When there are multiple versions of a single dependency, not only is there additional complexity in maintaining different versions of that dependency, there are also code size complications with bundling. Having multiple versions of a given dependency will likely result in bloated code size as each dependency version will need to be bundled independently. Having multiple versions might also leave developers confused and lead to possible security implications.
Additionally – keeping versions consistent reduces the possibility of type mismatches across the monorepo.
By default, this rule is disabled. Enable it by [customizing Conformance](https://vercel.com/docs/conformance/customize).
##  [How to fix](https://vercel.com/docs/conformance/rules/REQUIRE_ONE_VERSION_POLICY#how-to-fix)[](https://vercel.com/docs/conformance/rules/REQUIRE_ONE_VERSION_POLICY#how-to-fix)
Ensure all `package.json` files in your monorepo that have a `dependency` are aligned to all have the same version. Version ranges are not always reliable, so it's recommended that you pin all versions to the same given version to ensure consistency.
##  [Exceptions](https://vercel.com/docs/conformance/rules/REQUIRE_ONE_VERSION_POLICY#exceptions)[](https://vercel.com/docs/conformance/rules/REQUIRE_ONE_VERSION_POLICY#exceptions)
Sometimes it is useful to temporarily have two or more versions of a dependency whilst incrementally migrating a monorepo to having the same version policy. In which case, it's acceptable to allowlist this rule on specific parts of the codebase using by [customizing Conformance](https://vercel.com/docs/conformance/customize) until all packages have been successfully migrated.
* * *
Was this helpful?
Send
