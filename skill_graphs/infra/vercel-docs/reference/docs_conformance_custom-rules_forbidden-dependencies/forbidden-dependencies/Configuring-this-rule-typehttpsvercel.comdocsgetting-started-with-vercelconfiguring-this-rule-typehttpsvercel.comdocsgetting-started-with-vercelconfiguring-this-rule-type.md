##  [Configuring this rule type](https://vercel.com/docs/getting-started-with-vercel#configuring-this-rule-type)[](https://vercel.com/docs/getting-started-with-vercel#configuring-this-rule-type)
To create a custom `forbidden-dependencies` rule, you'll need to configure the required properties below:
Property | Type | Description
---|---|---
`ruleType` | `"forbidden-dependencies"` | The custom rule's type.
`ruleName` | `string` | The custom rule's name.
`categories` |  `("nextjs" | "performance" | "security" | "code-health")[]` (optional) | The custom rule's categories. Default is `["code-health"]`.
`errorMessage` | `string` | The error message, which is shown to users when they encounter this rule.
`errorLink` |  `string` (optional) | An optional link to show alongside the error message.
`description` |  `string` (optional) | The rule description, which is shown in the Vercel Compass dashboard and included in allowlist files.
`severity` |  `"major" | "minor"` (optional) | The rule severity added to the allowlists and used to calculate a project's conformance score.
`moduleNames` | `string[]` | An array of exact module names or glob expressions*.

_*Note that paths containing square brackets need to be escaped, i.e.`[folder-name]\page.tsx` would become `\[folder-name\]\page.tsx`._
`paths` |  `string[]` (optional) | An optional array of exact paths or glob expressions, which restricts the paths that this custom rule applies to. This acts as the overridable default value for `paths`*.

_*Note that paths containing square brackets need to be escaped, i.e.`[folder-name]\page.tsx` would become `\[folder-name\]\page.tsx`._
`traverseNodeModules` |  `boolean` (optional) | When `true`, this rule will also traverse `node_modules` for transient dependencies.
When using `traverseNodeModules`, module names currently need to be prefixed with `node_modules` (i.e., `["disallowed", "node_modules/disallowed"]`). We're working to improve this.
###  [Example configuration](https://vercel.com/docs/getting-started-with-vercel#example-configuration)[](https://vercel.com/docs/getting-started-with-vercel#example-configuration)
The example below configures a rule named `NO_SUPER_SECRET_IN_CLIENT` that disallows depending on any package from the `super-secret` workspace except for `@super-secret/safe-exports`.
conformance.config.jsonc
```
{
  "customRules": [
    {
      "ruleType": "forbidden-dependencies",
      "ruleName": "NO_SUPER_SECRET_IN_CLIENT",
      "categories": ["code-health"],
      "errorMessage": "Depending on packages from the 'super-secret' workspace may result in secrets being exposed in client-side code. Please use '@super-secret/safe-exports' instead.",
      "description": "Prevents depending on packages from the 'super-secret' workspace.",
      "severity": "major",
      "moduleNames": ["@super-secret/*", "!@super-secret/safe-exports"],
    },
  ],
}
```
