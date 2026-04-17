##  [Adding custom error messages to Conformance rules](https://vercel.com/docs/conformance/customize#adding-custom-error-messages-to-conformance-rules)[](https://vercel.com/docs/conformance/customize#adding-custom-error-messages-to-conformance-rules)
If you want to specify additional information or link to project-specific documentation, you can add custom error messages to the output of any conformance rule. These messages can be added globally to all rules or on a per-rule basis.
To add an error message to the output of all rules, add `globalErrorMessage` to the `configuration` section of the override:
conformance.config.jsonc
```
{
  "overrides": [
    {
      "configuration": {
        "globalErrorMessage": "See link_to_docs for more information.",
      },
    },
  ],
}
```

To add an error message to the output of one specific rule, add an entry for that test to the `additionalErrorMessages` field:
conformance.config.jsonc
```
{
  "overrides": [
    {
      "configuration": {
        "additionalErrorMessages": {
          "TYPESCRIPT_CONFIGURATION": "Please see project_link_to_typescript_docs for more information.",
        },
      },
    },
  ],
}
```

* * *
Was this helpful?
Send
On this page
  * [Enabling all rules By default](https://vercel.com/docs/conformance/customize#enabling-all-rules-by-default)
  * [Ignoring files](https://vercel.com/docs/conformance/customize#ignoring-files)
  * [Configuring specific workspaces](https://vercel.com/docs/conformance/customize#configuring-specific-workspaces)
  * [Configuration cascade](https://vercel.com/docs/conformance/customize#configuration-cascade)
  * [Managing a Conformance rule](https://vercel.com/docs/conformance/customize#managing-a-conformance-rule)
  * [Configuring a Conformance rule](https://vercel.com/docs/conformance/customize#configuring-a-conformance-rule)
  * [Adding custom error messages to Conformance rules](https://vercel.com/docs/conformance/customize#adding-custom-error-messages-to-conformance-rules)


Copy as MarkdownGive feedbackAsk AI about this page
