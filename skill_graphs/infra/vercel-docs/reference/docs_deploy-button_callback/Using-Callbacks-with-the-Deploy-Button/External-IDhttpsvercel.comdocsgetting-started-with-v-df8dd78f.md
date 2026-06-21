##  [External ID](https://vercel.com/docs/getting-started-with-vercel#external-id)[](https://vercel.com/docs/getting-started-with-vercel#external-id)
Parameter | Type | Value
---|---|---
`external-id` | `string` | An external ID or reference of your choice.
This parameter allows you to pass the ID or reference of your choice to the Project creation flow.
The query parameter will be relayed to the [Redirect URL](https://vercel.com/docs/integrations/create-integration) of each required [Integration](https://vercel.com/docs/integrations/deploy-button/integrations) when the user adds them in the Project creation flow.
To use this parameter, you also need to specify at least one [Integration](https://vercel.com/docs/integrations/deploy-button/integrations).
The example below shows a Deploy Button source URL using the Integration ID and External ID parameters:
external id
```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&integration-ids=oac_1mkAfc68cuDV4suZRlgkn3Re&external-id=1284210
```
