##  [Enabling this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-packages#enabling-this-rule-type)[](https://vercel.com/docs/conformance/custom-rules/forbidden-packages#enabling-this-rule-type)
The example below enables the `NO_TEAM_PACKAGES` custom rule. In this example, the custom rule is also restricted to the `dashboard` and `marketing-site` workspaces, which is optional.
conformance.config.jsonc
```
{
  "overrides": [
    {
      "restrictTo": {
        "workspaces": ["dashboard", "marketing-site"],
      },
      "rules": {
        "CUSTOM.NO_TEAM_PACKAGES": true,
      },
    },
  ],
  "customRules": [
    // ...
  ],
}
```

* * *
Was this helpful?
Send
On this page
  * [When to use this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-packages#when-to-use-this-rule-type)
  * [Configuring this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-packages#configuring-this-rule-type)
  * [Example configuration](https://vercel.com/docs/conformance/custom-rules/forbidden-packages#example-configuration)
  * [Enabling this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-packages#enabling-this-rule-type)


Copy as MarkdownGive feedbackAsk AI about this page
