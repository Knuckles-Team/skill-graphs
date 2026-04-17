##  [Enabling this rule type](https://vercel.com/docs/getting-started-with-vercel#enabling-this-rule-type)[](https://vercel.com/docs/getting-started-with-vercel#enabling-this-rule-type)
To enable this rule type, you can set the rule to `true`, or provide the following configuration.
Property | Type | Description
---|---|---
`paths` |  `string[]` (optional) | An optional array of exact paths or glob expressions, which restricts the paths that this custom rule applies to*.

_*Note that paths containing square brackets need to be escaped, i.e.`[folder-name]\page.tsx` would become `\[folder-name\]\page.tsx`._
The example below enables the `NO_SUPER_SECRET_IN_CLIENT` custom rule for all files in the `src/` directory, excluding test files. In this example, the custom rule is also restricted to the `dashboard` and `marketing-site` workspaces, which is optional.
conformance.config.jsonc
```
{
  "overrides": [
    {
      "restrictTo": {
        "workspaces": ["dashboard", "marketing-site"],
      },
      "rules": {
        "CUSTOM.NO_SUPER_SECRET_IN_CLIENT": {
          "paths": ["src", "!src/**/*.test.ts"],
        },
      },
    },
  ],
  "customRules": [
    // ...
  ],
}
```

This next example enables the `NO_SUPER_SECRET_IN_CLIENT` custom rule for all files, and without workspace restrictions.
conformance.config.jsonc
```
{
  "overrides": [
    {
      "rules": {
        "CUSTOM.NO_SUPER_SECRET_IN_CLIENT": true,
      },
    },
  ],
  "customRules": [
    // ...
  ],
}
```

* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [When to use this rule type](https://vercel.com/docs/getting-started-with-vercel#when-to-use-this-rule-type)
  * [Configuring this rule type](https://vercel.com/docs/getting-started-with-vercel#configuring-this-rule-type)
  * [Example configuration](https://vercel.com/docs/getting-started-with-vercel#example-configuration)
  * [Enabling this rule type](https://vercel.com/docs/getting-started-with-vercel#enabling-this-rule-type)


Copy as MarkdownGive feedbackAsk AI about this page
