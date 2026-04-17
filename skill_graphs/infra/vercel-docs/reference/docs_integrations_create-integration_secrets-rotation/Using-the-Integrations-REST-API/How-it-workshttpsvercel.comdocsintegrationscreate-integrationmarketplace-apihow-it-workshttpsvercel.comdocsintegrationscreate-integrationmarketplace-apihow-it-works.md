##  [How it works](https://vercel.com/docs/integrations/create-integration/marketplace-api#how-it-works)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#how-it-works)
When a customer uses your integration, the following two APIs are used for interaction and communication between the user, Vercel and the provider integration:
  * Vercel calls the provider API: You implement the [Vercel Marketplace Partner API](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/partner) endpoints on your integration server. Vercel calls them to manage resources, handle installations, and process billing.
  * The provider calls the Vercel API: Vercel provides [these endpoints](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel). You call them from your integration server to interact with Vercel's platform.


When building your integration, you'll implement the partner endpoints and call the Vercel endpoints as needed.
See the [Native Integration Flows](https://vercel.com/docs/integrations/create-integration/marketplace-flows) to understand how these endpoints work together.
