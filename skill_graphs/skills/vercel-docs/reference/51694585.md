##  [Resources](https://vercel.com/docs/integrations/create-integration/native-integration#resources)[](https://vercel.com/docs/integrations/create-integration/native-integration#resources)
Resources are the actual instances of products that integration users provision and utilize. They represent instances of products in your system, like databases or other infrastructure the user provisions in your service. Resources provide the flexibility and granularity needed for users to tailor the integration to their specific needs and project structures.
Resources track usage and billing at the individual resource level, giving you the ability to monitor and charge for each provisioned instance separately.
Concept | Definition
---|---
Resource | A specific instance of a product provisioned in an installation.
Provisioning | Explicit creation and removal (de-provisioning) of resources by users.
Keysets | Independent sets of secrets for each resource.
Project connection | Ability to link resources to Vercel projects independently.
###  [Working with installation and team information](https://vercel.com/docs/integrations/create-integration/native-integration#working-with-installation-and-team-information)[](https://vercel.com/docs/integrations/create-integration/native-integration#working-with-installation-and-team-information)
When working with resources, you'll use the `installationId` as the main identifier for connecting resources to a team's installation. Note that Vercel does not provide a `teamId` directly. Instead, use the [Get Account Information endpoint](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel/get-account-info) with the `installationId` to retrieve current team contact information and other account details.
###  [Resource usage patterns](https://vercel.com/docs/integrations/create-integration/native-integration#resource-usage-patterns)[](https://vercel.com/docs/integrations/create-integration/native-integration#resource-usage-patterns)
Integration users can add and manage resources in various ways. For example:
  * Single resource: Using one resource such as one database for all projects.
  * Per-project resources: Dedicating separate resources for each project.
  * Environment-specific resources: Using separate resources for different environments (development, preview, production) within a project.
