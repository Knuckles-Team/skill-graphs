##  [Configuring this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#configuring-this-rule-type)[](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#configuring-this-rule-type)
To create a custom `forbidden-properties` rule, you'll need to configure the below required properties:
Property | Type | Description
---|---|---
`ruleType` | `"forbidden-properties"` | The custom rule's type.
`ruleName` | `string` | The custom rule's name.
`errorMessage` | `string` | The error message, which is shown to users when they encounter this rule.
`errorLink` |  `string` (optional) | An optional link to show alongside the error message.
`description` |  `string` (optional) | The rule description, which is shown in the Vercel Compass dashboard and included in allowlist files.
`severity` |  `"major" | "minor"` (optional) | The rule severity added to the allowlists and used to calculate a project's conformance score.
`forbiddenProperties` | [`ForbiddenProperty[]`](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#forbiddenproperty) | One or more properties and their forbidden operations.
###  [`ForbiddenProperty`](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#forbiddenproperty)[](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#forbiddenproperty)
Property | Type | Description
---|---|---
`property` | `string` | The property to target.
`operations` | `{ call?: boolean, read?: boolean, write?: boolean }` | The operation(s) to target. At least one operation is required.
###  [Example configuration](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#example-configuration)[](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#example-configuration)
The example below configures a rule named `NO_DOCUMENT_WRITE_CALLS` that disallows calling `document.write`.
conformance.config.jsonc
```
{
  "customRules": [
    {
      "ruleType": "forbidden-properties",
      "ruleName": "NO_DOCUMENT_WRITE_CALLS",
      "errorMessage": "Calling 'document.write' is not allowed.",
      "description": "Disallows calls to `document.write`.",
      "severity": "major",
      "forbiddenProperties": [
        {
          "property": "document.write",
          "operations": {
            "call": true,
          },
        },
      ],
    },
  ],
}
```

###  [Property assignments](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#property-assignments)[](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#property-assignments)
Note that a property's assignments are tracked by this custom rule type.
Using our example `NO_DOCUMENT_WRITE_CALLS` rule (above), the following calls will both result in errors.
```
document.write();

const writer = document.write;
writer();
```
