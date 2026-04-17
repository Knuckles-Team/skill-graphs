##  [Enabling this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#enabling-this-rule-type)[](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#enabling-this-rule-type)
The example below enables the `NO_DOCUMENT_WRITE_CALLS` custom rule. In this example, the custom rule is also restricted to the `dashboard` and `marketing-site` workspaces, which is optional.
conformance.config.jsonc
```
{
  "overrides": [
    {
      "restrictTo": {
        "workspaces": ["dashboard", "marketing-site"],
      },
      "rules": {
        "CUSTOM.NO_DOCUMENT_WRITE_CALLS": true,
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
  * [When to use this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#when-to-use-this-rule-type)
  * [Configuring this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#configuring-this-rule-type)
  * [ForbiddenProperty](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#forbiddenproperty)
  * [Example configuration](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#example-configuration)
  * [Property assignments](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#property-assignments)
  * [Enabling this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#enabling-this-rule-type)


Copy as MarkdownGive feedbackAsk AI about this page
