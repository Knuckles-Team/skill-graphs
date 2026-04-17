##  [Configuring this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-code#configuring-this-rule-type)[](https://vercel.com/docs/conformance/custom-rules/forbidden-code#configuring-this-rule-type)
To create a custom `forbidden-code` rule, you'll need to configure the below required properties:
Property | Type | Description
---|---|---
`ruleType` | `"forbidden-code"` | The custom rule's type.
`ruleName` | `string` | The custom rule's name.
`categories` |  `("nextjs" | "performance" | "security" | "code-health")[]` (optional) | The custom rule's categories. Default is `["code-health"]`.
`errorMessage` | `string` | The error message, which is shown to users when they encounter this rule.
`errorLink` |  `string` (optional) | An optional link to show alongside the error message.
`description` |  `string` (optional) | The rule description, which is shown in the Vercel Compass dashboard and included in allowlist files.
`severity` |  `"major" | "minor"` (optional) | The rule severity added to the allowlists and used to calculate a project's conformance score.
`patterns` | `(string | { pattern: string, flags: string })[]` | An array of regular expression patterns to match against.
`strings` | `string[]` | An array of exact string to match against (case sensitive).
Multi-line strings and patterns are currently unsupported by this custom rule type.
###  [Example configuration](https://vercel.com/docs/conformance/custom-rules/forbidden-code#example-configuration)[](https://vercel.com/docs/conformance/custom-rules/forbidden-code#example-configuration)
The example below configures a rule named `NO_DISALLOWED_USAGE` that disallows:
  * Any usage of `"and"` at the start of a line (case-sensitive).
  * Any usage of `"but"` in any case.
  * Any usage of `"TODO"` (case-sensitive).


conformance.config.jsonc
```
{
  "customRules": [
    {
      "ruleType": "forbidden-imports",
      "ruleName": "NO_DISALLOWED_USAGE",
      "categories": ["code-health"],
      "errorMessage": "References to \"and\" at the start of a line are not allowed.",
      "description": "Disallows using \"and\" at the start of a line.",
      "severity": "major",
      "patterns": ["^and", { "pattern": "but", "flags": "i" }],
      "strings": ["TODO"],
    },
  ],
}
```

###  [Using flags with patterns](https://vercel.com/docs/conformance/custom-rules/forbidden-code#using-flags-with-patterns)[](https://vercel.com/docs/conformance/custom-rules/forbidden-code#using-flags-with-patterns)
This custom rule type always sets the `"g"` (or global) flag for regular expressions. This ensures that all regular expression matches are reported, opposed to only reporting on the first match.
When providing flags through an object in `patterns`, you can omit the `"g"` as this will automatically be set.
To learn more about regular expression flags, see
###  [Writing patterns](https://vercel.com/docs/conformance/custom-rules/forbidden-code#writing-patterns)[](https://vercel.com/docs/conformance/custom-rules/forbidden-code#writing-patterns)
If you're not familiar with regular expressions, you can use tools like
Regular expressions can vary in complexity, depending on what you're trying to achieve. We've added some examples below to help you get started.
Pattern | Description
---|---
`^and` | Matches `"and"`, but only if it occurs at the start of a line (`^`).
`(B|a)ar$` | Matches `"But"` and `"but"`, but only if it occurs at the end of a line (`$`).
`regexp?` | Matches `"regexp"` and `"regex"`, with or without the `"p"` (`?`).
`(?<!-)so` | Matches `"so"`, but only when not following a hyphen (`(?<!-)`).
