##  [Enabling all rules By default](https://vercel.com/docs/conformance/customize#enabling-all-rules-by-default)[](https://vercel.com/docs/conformance/customize#enabling-all-rules-by-default)
To enable all Conformance rules by default, add the `defaultRules` field to the top level `configuration` section of the config file:
conformance.config.jsonc
```
{
  "configuration": {
    "defaultRules": "all",
  },
}
```
