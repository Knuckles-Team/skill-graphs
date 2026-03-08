##  [Managing a Conformance rule](https://vercel.com/docs/conformance/customize#managing-a-conformance-rule)[](https://vercel.com/docs/conformance/customize#managing-a-conformance-rule)
To enable or disable a Conformance rule, use the `rules` field. This field is an object literal where the keys are the name of the [rule](https://vercel.com/docs/conformance/rules) and the values are booleans or another object literal containing a [rule-specific configuration](https://vercel.com/docs/conformance/customize#configuring-a-conformance-rule).
For example, this configuration will disable the `TYPESCRIPT_CONFIGURATION` rule:
conformance.config.jsonc
```
{
  "overrides": [
    {
      "rules": {
        "TYPESCRIPT_CONFIGURATION": false,
      },
    },
  ],
}
```

All rules are enabled by default unless explicitly disabled in the config.
