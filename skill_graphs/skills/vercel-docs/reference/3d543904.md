##  [Required Integrations](https://vercel.com/docs/deploy-button/integrations#required-integrations)[](https://vercel.com/docs/deploy-button/integrations#required-integrations)
Parameter | Type | Value
---|---|---
`integration-ids` | `string[]` | A comma-separated list of required Integrations IDs: `oac_4mkAfc68cuDV4suZRlgkn3R9, oac_JI9dt8xHo7UXmVV6mZTygMNZ`
This parameter allows you to specify a list of Integration IDs. When specified, the corresponding Integrations will be required to be added before the Project can be imported. You can add up to 3 Integrations per Project.
You can find the IDs of your Integrations in the [Integrations Console](https://vercel.com/dashboard/integrations/console).
The example below shows how to use the `integration-ids` parameter in a Deploy Button source URL:
integration id
```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&integration-ids=oac_1mkAfc68cuDV4suZRlgkn3Re
```
