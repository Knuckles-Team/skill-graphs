##  [Configuring this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-imports#configuring-this-rule-type)[](https://vercel.com/docs/conformance/custom-rules/forbidden-imports#configuring-this-rule-type)
To create a custom `forbidden-imports` rule, you'll need to configure the below required properties:
Property | Type | Description
---|---|---
`ruleType` | `"forbidden-imports"` | The custom rule's type.
`ruleName` | `string` | The custom rule's name.
`categories` |  `("nextjs" | "performance" | "security" | "code-health")[]` (optional) | The custom rule's categories. Default is `["code-health"]`.
`errorMessage` | `string` | The error message, which is shown to users when they encounter this rule.
`errorLink` |  `string` (optional) | An optional link to show alongside the error message.
`description` |  `string` (optional) | The rule description, which is shown in the Vercel Compass dashboard and included in allowlist files.
`severity` |  `"major" | "minor"` (optional) | The rule severity added to the allowlists and used to calculate a project's conformance score.
`moduleNames` | `string[]` | An array of exact module names or glob expressions*.

_*Note that paths containing square brackets need to be escaped, i.e.`[folder-name]\page.tsx` would become `\[folder-name\]\page.tsx`._
`importNames` |  `string[]` (optional) | An array of exact module names of import names.
`paths` |  `string[]` (optional) |  Added in Conformance `1.4.0`. An optional array of exact paths or glob expressions, which restricts the paths that this custom rule applies to. This acts as the overridable default value for `paths`*.

_*Note that paths containing square brackets need to be escaped, i.e.`[folder-name]\page.tsx` would become `\[folder-name\]\page.tsx`._
`disallowDefaultImports` |  `boolean` (optional) | Flags default imports (i.e. `import foo from 'foo';`) as errors.
`disallowNamespaceImports` |  `boolean` (optional) | Flags namespace imports (i.e. `import * as foo from 'foo';`) as errors.
Note that when using `moduleNames` alone, imports are not allowed at all from that module. When used with conditions like `importNames`, the custom rule will only report an error when those conditions are also met.
###  [Example configuration](https://vercel.com/docs/conformance/custom-rules/forbidden-imports#example-configuration)[](https://vercel.com/docs/conformance/custom-rules/forbidden-imports#example-configuration)
The example below configures a rule named `NO_TEAM_IMPORTS` that disallows importing any package from the `team` workspace except for `@team/utils`. It also configures a rule that disallows importing `oldMethod` from `@team/utils`, but restricts that rule to the `src/new/` directory.
conformance.config.jsonc
```
{
  "customRules": [
    {
      "ruleType": "forbidden-imports",
      "ruleName": "NO_TEAM_IMPORTS",
      "categories": ["security"],
      "errorMessage": "Packages from the team workspace have been deprecated in favour of '@team/utils'.",
      "description": "Disallows importing packages from the team workspace.",
      "severity": "major",
      "moduleNames": ["@team/*", "!@team/utils"],
    },
    {
      "ruleType": "forbidden-imports",
      "ruleName": "NO_TEAM_OLD_METHOD_IMPORTS",
      "categories": ["performance"],
      "errorMessage": "'oldMethod' has been deprecated in favour of 'newMethod'.",
      "description": "Disallows using the deprecated method 'oldMethod' from '@team/utils'.",
      "severity": "minor",
      "moduleNames": ["@team/utils"],
      "importNames": ["oldMethod"],
      "paths": ["src/new/**"],
    },
  ],
}
```
