##  [Configuring a Conformance rule](https://vercel.com/docs/conformance/customize#configuring-a-conformance-rule)[](https://vercel.com/docs/conformance/customize#configuring-a-conformance-rule)
Some Conformance rules can be configured to alter behavior based on the project settings. Instead of a `boolean` being provided in the `rules` configuration, an object literal could be passed with the configuration for that rule.
For example, this configuration will require a specific list of ESLint plugins in every workspace:
conformance.config.jsonc
```
{
  "overrides": [
    {
      "rules": {
        "ESLINT_CONFIGURATION": {
          "requiredPlugins": ["@typescript-eslint"],
        },
      },
    },
  ],
}
```
