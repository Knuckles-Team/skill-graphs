##  [Enabling this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-code#enabling-this-rule-type)[](https://vercel.com/docs/conformance/custom-rules/forbidden-code#enabling-this-rule-type)
To enable this rule type, you can set the rule to `true`, or provide the following configuration.
Property | Type | Description
---|---|---
`paths` |  `string[]` (optional) | An optional array of exact paths or glob expressions*.

_*Note that paths containing square brackets need to be escaped, i.e.`[folder-name]\page.tsx` would become `\[folder-name\]\page.tsx`._
The example below enables the `NO_DISALLOWED_USAGE` custom rule for all files in the `src/` directory, excluding files in `src/legacy/`. In this example, the custom rule is also restricted to the `dashboard` and `marketing-site` workspaces, which is optional.
conformance.config.jsonc
```
{
  "overrides": [
    {
      "restrictTo": {
        "workspaces": ["dashboard", "marketing-site"],
      },
      "rules": {
        "CUSTOM.NO_DISALLOWED_USAGE": {
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

This next example enables the `NO_DISALLOWED_USAGE` custom rule for all files, and without workspace restrictions.
conformance.config.jsonc
```
{
  "overrides": [
    {
      "rules": {
        "CUSTOM.NO_DISALLOWED_USAGE": true,
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
  * [When to use this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-code#when-to-use-this-rule-type)
  * [Configuring this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-code#configuring-this-rule-type)
  * [Example configuration](https://vercel.com/docs/conformance/custom-rules/forbidden-code#example-configuration)
  * [Using flags with patterns](https://vercel.com/docs/conformance/custom-rules/forbidden-code#using-flags-with-patterns)
  * [Writing patterns](https://vercel.com/docs/conformance/custom-rules/forbidden-code#writing-patterns)
  * [Enabling this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-code#enabling-this-rule-type)


Copy as MarkdownGive feedbackAsk AI about this page
