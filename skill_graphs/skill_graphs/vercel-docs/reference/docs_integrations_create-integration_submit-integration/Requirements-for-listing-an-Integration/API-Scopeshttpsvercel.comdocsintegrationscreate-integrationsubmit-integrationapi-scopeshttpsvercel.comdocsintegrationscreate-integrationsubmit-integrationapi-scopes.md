##  [API Scopes](https://vercel.com/docs/integrations/create-integration/submit-integration#api-scopes)[](https://vercel.com/docs/integrations/create-integration/submit-integration#api-scopes)
  * Required: No


API Scopes define the level of access your integration will have to the Vercel REST API. When setting up a new integration, you need to:
  * Select only the API Scopes that are essential for your integration to function
  * Choose the appropriate permission level for each scope: `None`, `Read`, or `Read/Write`


After activation, your integration may collect specific user data based on the selected scopes. You are accountable for:
  * The privacy, security, and integrity of this user data
  * Compliance with [Vercel's Shared Responsibility Model](https://vercel.com/docs/security/shared-responsibility#shared-responsibilities)

![Select API Scopes for your integration.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fcreating%2Fapi-scopes-light.png&w=1920&q=75)![Select API Scopes for your integration.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fcreating%2Fapi-scopes-dark.png&w=1920&q=75)Select API Scopes for your integration.
Learn more about API scope permissions in the [Extending Vercel](https://vercel.com/docs/integrations/install-an-integration/manage-integrations-reference) documentation.
