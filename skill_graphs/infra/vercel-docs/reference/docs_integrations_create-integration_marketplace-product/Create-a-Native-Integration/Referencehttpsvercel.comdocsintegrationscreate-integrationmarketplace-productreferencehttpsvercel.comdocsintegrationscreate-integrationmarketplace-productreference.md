##  [Reference](https://vercel.com/docs/integrations/create-integration/marketplace-product#reference)[](https://vercel.com/docs/integrations/create-integration/marketplace-product#reference)
###  [Metadata schema](https://vercel.com/docs/integrations/create-integration/marketplace-product#metadata-schema)[](https://vercel.com/docs/integrations/create-integration/marketplace-product#metadata-schema)
When you first create your product, you will see a Metadata Schema field of the product configuration options. You will edit this schema to match the options you want to make available in the Vercel integration dashboard to the customer who installs this product integration.
When the customer installs your product, Vercel collects data from this customer and sends it to your integration server based on the Metadata schema you provided in the product configuration. The schema includes properties specific to Vercel that allow the Vercel dashboard to understand how to render the user interface to collect this data from the customer.
As an example, use the following configuration to only show the name of the product:
```
{
  "type": "object",
  "properties": {},
  "additionalProperties": false,
  "required": []
}
```

See the endpoints for [Provision](https://vercel.com/docs/integrations/marketplace-api#provision-resource) or [Update](https://vercel.com/docs/integrations/marketplace-api#update-resource) Resource for specific examples.
Property `ui:control` | Property `type` | Notes
---|---|---
`input` | `number` | Number input
`input` | `string` | Text input
`toggle` | `boolean` | Toggle input
`slider` | `array` | Slider input. The `items` property of your array must have a type of number
`select` | `string` | Dropdown input
`multi-select` | `array` | Dropdown with multi-select input. The items property of your array must have a type of string
`vercel-region` | `string` | Vercel Region dropdown input. You can restrict the list of available regions by settings the acceptable regions in the enum property
`multi-vercel-region` | `array` | Vercel Region dropdown with multi-select input. You can restrict the list of available regions by settings the acceptable regions in the enum property of your items. Your items property must have type of string
`domain` | `string` | Domain name input
`git-namespace` | `string` | Git namespace selector
This table shows the possible keys for the `properties` object that each represent a type of `ui:control` that is a form element to be used on the Vercel dashboard for this property.
See the [full JSON schema](https://vercel.com/api/v1/integrations/marketplace/metadata-schema) for the Metadata Schema. You can add it to your code editor for autocomplete and validation.
You can add it to your editor configuration as follows:
```
{
  "$schema": "https://vercel.com/api/v1/integrations/marketplace/metadata-schema"
}
```
