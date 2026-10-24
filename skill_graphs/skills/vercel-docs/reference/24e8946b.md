##  [Integrations Agreement](https://vercel.com/docs/integrations/create-integration/submit-integration#integrations-agreement)[](https://vercel.com/docs/integrations/create-integration/submit-integration#integrations-agreement)
  * Required:
    * Yes: If it's a connectable account integration or this is the first time you are creating a native integration
    * No: If you are adding a product to the integration. A different agreement may be needed for the first added product


You must agree to the Vercel terms before your integration can be published. The terms may differ depending the type of integration, [connectable account](https://vercel.com/docs/integrations/create-integration#connectable-account-integrations) or [native](https://vercel.com/docs/integrations#native-integrations).
###  [Marketplace installation flow](https://vercel.com/docs/integrations/create-integration/submit-integration#marketplace-installation-flow)[](https://vercel.com/docs/integrations/create-integration/submit-integration#marketplace-installation-flow)
Usage Scenario: For installations initiated from the [Vercel Marketplace](https://vercel.com/integrations).
  * Post-Installation: After installation, the user is redirected to a page on your side to complete the setup
  * Completion: Redirect the user to the provided next URL to close the popup and continue


####  [Query parameters for marketplace](https://vercel.com/docs/integrations/create-integration/submit-integration#query-parameters-for-marketplace)[](https://vercel.com/docs/integrations/create-integration/submit-integration#query-parameters-for-marketplace)
Name | Definition | Example
---|---|---
code | The code you received. | `jMIukZ1DBCKXHje3X14BCkU0`
teamId | The ID of the team (only if a team is selected). | `team_LLHUOMOoDlqOp8wPE4kFo9pE`
configurationId | The ID of the configuration. | `icfg_6uKSUQ359QCbPfECTAY9murE`
next | Encoded URL to redirect to, once the installation process on your side is finished. | `https%3A%2F%2Fvercel.com%2F...`
source | Source defines where the integration was installed from. | `marketplace`
###  [External installation flow](https://vercel.com/docs/integrations/create-integration/submit-integration#external-installation-flow)[](https://vercel.com/docs/integrations/create-integration/submit-integration#external-installation-flow)
Usage Scenario: When you're initiating the installation from your application.
  * Starting Point: Use this URL to start the process: `https://vercel.com/integrations/:slug/new` - `:slug` is the name you added in the [Create Integration form](https://vercel.com/docs/integrations/create-integration#create-integration-form-details)


####  [Query parameters for external flow](https://vercel.com/docs/integrations/create-integration/submit-integration#query-parameters-for-external-flow)[](https://vercel.com/docs/integrations/create-integration/submit-integration#query-parameters-for-external-flow)
Name | Definition | Example
---|---|---
code | The code you received. | `jMIukZ1DBCKXHje3X14BCkU0`
teamId | The ID of the team (only if a team is selected). | `team_LLHUOMOoDlqOp8wPE4kFo9pE`
configurationId | The ID of the configuration. | `icfg_6uKSUQ359QCbPfECTAY9murE`
next | Encoded URL to redirect to, once the installation process on your side is finished. | `https%3A%2F%2Fvercel.com%2F...`
state | Random string to be passed back upon completion. It is used to protect against CSRF attacks. | `xyzABC123`
source | Source defines where the integration was installed from. | `external`
###  [Deploy button installation flow](https://vercel.com/docs/integrations/create-integration/submit-integration#deploy-button-installation-flow)[](https://vercel.com/docs/integrations/create-integration/submit-integration#deploy-button-installation-flow)
Usage Scenario: For installations using the [Vercel deploy button](https://vercel.com/docs/deploy-button).
  * Post-Installation: The user will complete the setup on your side
  * Completion: Redirect the user to the provided next URL to proceed


####  [Query Parameters for Deploy Button](https://vercel.com/docs/integrations/create-integration/submit-integration#query-parameters-for-deploy-button)[](https://vercel.com/docs/integrations/create-integration/submit-integration#query-parameters-for-deploy-button)
Name | Definition | Example
---|---|---
code | The code you received. | `jMIukZ1DBCKXHje3X14BCkU0`
teamId | The ID of the team (only if a team is selected). | `team_LLHUOMOoDlqOp8wPE4kFo9pE`
configurationId | The ID of the configuration. | `icfg_6uKSUQ359QCbPfECTAY9murE`
next | Encoded URL to redirect to, once the installation process on your side is finished. | `https%3A%2F%2Fvercel.com%2F...`
currentProjectId | The ID of the created project. | `QmXGTs7mvAMMC7WW5ebrM33qKG32QK3h4vmQMjmY`
external-id | Reference of your choice. See [External ID](https://vercel.com/docs/deploy-button/callback#external-id) for more details. | `1284210`
source | Source defines where the integration was installed from. | `deploy-button`
If the integration is already installed in the selected scope during the deploy button flow, the redirect URL will be called with the most recent `configurationId`.
Make sure to store `configurationId` along with an access token such that if an existing `configurationId` was passed, you could retrieve the corresponding access token.
