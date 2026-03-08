##  [Configuring this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-packages#configuring-this-rule-type)[](https://vercel.com/docs/conformance/custom-rules/forbidden-packages#configuring-this-rule-type)
To create a custom `forbidden-packages` rule, you'll need to configure the below required properties:
Property | Type | Description
---|---|---
`ruleType` | `"forbidden-packages"` | The custom rule's type.
`ruleName` | `string` | The custom rule's name.
`categories` |  `("nextjs" | "performance" | "security" | "code-health")[]` (optional) | The custom rule's categories. Default is `["code-health"]`.
`errorMessage` | `string` | The error message, which is shown to users when they encounter this rule.
`errorLink` |  `string` (optional) | An optional link to show alongside the error message.
`description` |  `string` (optional) | The rule description, which is shown in the Vercel Compass dashboard and included in allowlist files.
`severity` |  `"major" | "minor"` (optional) | The rule severity added to the allowlists and used to calculate a project's conformance score.
`packageNames` | `string[]` | An array of exact package names or glob expressions.
`packageVersions` |  `string[]` (optional) |  Added in Conformance `1.8.0`. An optional array of exact package versions or
###  [Example configuration](https://vercel.com/docs/conformance/custom-rules/forbidden-packages#example-configuration)[](https://vercel.com/docs/conformance/custom-rules/forbidden-packages#example-configuration)
The example below configures a rule named `NO_TEAM_PACKAGES` that disallows importing any package from the `team` workspace except for `@team/utils`.
conformance.config.jsonc
```
{
  "customRules": [
    {
      "ruleType": "forbidden-packages",
      "ruleName": "NO_TEAM_PACKAGES",
      "errorMessage": "Packages from the team workspace have been deprecated in favour of '@team/utils'.",
      "description": "Disallow importing packages from the team workspace.",
      "severity": "major",
      "packageNames": ["@team/*", "!@team/utils"],
    },
  ],
}
```

The next example restricts the `utils` package, only allowing versions equal to or above `2.0.0`. This option requires Conformance `1.8.0` or later.
conformance.config.jsonc
```
{
  "customRules": [
    {
      "ruleType": "forbidden-packages",
      "ruleName": "NO_OLD_UTIL_PACKAGES",
      "errorMessage": "Versions of `utils` below `2.0.0` are not allowed for security reasons.",
      "description": "Disallow importing `utils` versions below version `2.0.0`.",
      "severity": "major",
      "packageNames": ["utils"],
      "packageVersions: ["<=2.0.0"]
    },
  ],
}
```
