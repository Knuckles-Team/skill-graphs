##  [When to use this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-imports#when-to-use-this-rule-type)[](https://vercel.com/docs/conformance/custom-rules/forbidden-imports#when-to-use-this-rule-type)
  * Deprecating packages or versions
    * You want to disallow importing a deprecated package, and to recommend a different approach
  * Recommending an alternative package
    * You want to require that users import custom/wrapped methods from `test-utils` instead of directly from a testing library


If you want to prevent depending on a module for performance or security reasons, you should instead use the [`forbidden-dependencies`](https://vercel.com/docs/conformance/custom-rules/forbidden-dependencies) rule type.
