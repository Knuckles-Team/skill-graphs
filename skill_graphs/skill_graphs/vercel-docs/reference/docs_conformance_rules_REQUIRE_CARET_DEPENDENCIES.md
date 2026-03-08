Menu
Menu
# REQUIRE_CARET_DEPENDENCIES
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule is available from version 1.4.0.
Using a caret ("^") as a prefix in the version of your dependencies is recommended. `"dependencies"` and `"devDependencies"`, and it helps maintain the security and health of your codebase.
By default, this rule is disabled. To enable it, refer to [customizing Conformance](https://vercel.com/docs/conformance/customize).
##  [Examples](https://vercel.com/docs/conformance/rules/REQUIRE_CARET_DEPENDENCIES#examples)[](https://vercel.com/docs/conformance/rules/REQUIRE_CARET_DEPENDENCIES#examples)
This rule will catch any `package.json` files:
  * Using `~` or `*` as a prefix of the version, like `~1.0.0`.
  * Version without a prefix, such as `1.0.0`.


package.json
```
{
  "dependencies": {
    "chalk": "~5.3.0",
    "ms": "*2.1.3",
  },
  "devDependencies": {
    "semver": "7.6.0"
  },
}
```

##  [How to fix](https://vercel.com/docs/conformance/rules/REQUIRE_CARET_DEPENDENCIES#how-to-fix)[](https://vercel.com/docs/conformance/rules/REQUIRE_CARET_DEPENDENCIES#how-to-fix)
If you hit this issue, you can resolve it by adding a `"^"` to the version of your dependency. If you want to keep using a pinned version, or another prefix, you can include the dependency in the [Allowlist](https://vercel.com/docs/conformance/allowlist).
package.json
```
{
  "dependencies": {
    "semver": "^7.6.0"
  },
}
```

* * *
Was this helpful?
Send
