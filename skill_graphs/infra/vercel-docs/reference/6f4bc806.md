##  [Skippable Integrations](https://vercel.com/docs/deploy-button/integrations#skippable-integrations)[](https://vercel.com/docs/deploy-button/integrations#skippable-integrations)
Parameter | Type | Value
---|---|---
`skippable-integrations` | `number` | Mark the list of provided Integrations as optional
If this parameter is present, the user will be able to add one of the provided Integrations or skip them entirely, instead of being forced to add all of them.
Because the user will only be able to select one (not multiple) of the optional Integrations, they should all serve the same purpose. For example, if the purpose is error tracking, the Integrations [Sentry](https://vercel.com/marketplace/sentry) and [Datadog](https://vercel.com/marketplace/datadog) could be defined here.
To use this parameter, you also need to specify at least one Integration.
The example below shows how to use the `skippable-integrations` parameter in a Deploy Button source URL:
skippable integrations
```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&integration-ids=oac_1mkAfc68cuDV4suZRlgkn3Re&skippable-integrations=1
```

* * *
Was this helpful?
Send
On this page
  * [Required Integrations](https://vercel.com/docs/deploy-button/integrations#required-integrations)
  * [Skippable Integrations](https://vercel.com/docs/deploy-button/integrations#skippable-integrations)


Copy as MarkdownGive feedbackAsk AI about this page
