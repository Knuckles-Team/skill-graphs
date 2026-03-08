##  [Common Errors](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#common-errors)[](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#common-errors)
When using the Vercel REST API with Integrations, you might come across some errors which you can address immediately.
###  [CORS issues](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#cors-issues)[](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#cors-issues)
To avoid CORS issues, make sure you only interact with the Vercel REST API on the server side.
Since the token grants access to resources of the Team or Personal Account, you should never expose it on the client side.
For more information on using CORS with Vercel, see [How can I enable CORS on Vercel?](https://vercel.com/kb/guide/how-to-enable-cors).
###  [403 Forbidden responses](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#403-forbidden-responses)[](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#403-forbidden-responses)
Ensure you are not missing the `teamId` [query parameter](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-url). `teamId` is required if the integration installation is for a Team. Ensure the Scope of Your [Access Token](https://vercel.com/docs/rest-api/vercel-api-integrations#using-the-vercel-api/scopes/teams) is properly set.
