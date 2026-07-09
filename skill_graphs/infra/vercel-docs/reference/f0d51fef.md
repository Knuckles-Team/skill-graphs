##  [When to use this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-packages#when-to-use-this-rule-type)[](https://vercel.com/docs/conformance/custom-rules/forbidden-packages#when-to-use-this-rule-type)
  * Deprecating packages
    * You want to disallow importing a deprecated package, and to recommend a different approach
  * Standardization
    * You want to ensure that projects depend on the same set of packages when performing similar tasks (i.e. using `jest` or `vitest` consistently across a monorepo)
  * Visibility and approval
    * You want to enable a workflow where team-owned packages can't be depended upon without acknowledgement or approval from that team. This helps owning teams to better plan and understand the impacts of their work
