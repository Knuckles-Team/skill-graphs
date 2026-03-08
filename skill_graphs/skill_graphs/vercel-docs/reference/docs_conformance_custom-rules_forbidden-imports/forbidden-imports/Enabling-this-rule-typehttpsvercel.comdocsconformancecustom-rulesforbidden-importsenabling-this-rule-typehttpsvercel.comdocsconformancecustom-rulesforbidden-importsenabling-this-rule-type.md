##  [Enabling this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-imports#enabling-this-rule-type)[](https://vercel.com/docs/conformance/custom-rules/forbidden-imports#enabling-this-rule-type)
To enable this rule type, you can set the rule to `true`, or provide the following configuration.
Property | Type | Description
---|---|---
`paths` |  `string[]` (optional) | An optional array of exact paths or glob expressions, which restricts the paths that this custom rule applies to*.

_*Note that paths containing square brackets need to be escaped, i.e.`[folder-name]\page.tsx` would become `\[folder-name\]\page.tsx`._
The example below enables the `NO_TEAM_IMPORTS` custom rule for all files in the `src/` directory, excluding files in `src/legacy/`. In this example, the custom rule is also restricted to the `dashboard` and `marketing-site` workspaces, which is optional.
conformance.config.jsonc
```
{
  "overrides": [
    {
      "restrictTo": {
        "workspaces": ["dashboard", "marketing-site"],
      },
      "rules": {
        "CUSTOM.NO_TEAM_IMPORTS": {
          "paths": ["src", "!src/legacy"],
        },
      },
    },
  ],
  "customRules": [
    // ...
  ],
}
```

;
* * *
Was this helpful?
Send
On this page
  * [When to use this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-imports#when-to-use-this-rule-type)
  * [Configuring this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-imports#configuring-this-rule-type)
  * [Example configuration](https://vercel.com/docs/conformance/custom-rules/forbidden-imports#example-configuration)
  * [Enabling this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-imports#enabling-this-rule-type)


Copy as MarkdownGive feedbackAsk AI about this page
