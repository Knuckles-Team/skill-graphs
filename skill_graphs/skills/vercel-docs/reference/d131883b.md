##  [Creating an integration](https://vercel.com/docs/integrations/create-integration#creating-an-integration)[](https://vercel.com/docs/integrations/create-integration#creating-an-integration)
Integrations can be created by filling out the Create Integration form. To access the form:
  1. From your Vercel [dashboard](https://vercel.com/d?to=%2Fdashboard&title=Open+Dashboard), select your account/team from the team switcher
  2. Open [Integrations](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fintegrations&title=Go+to+Integrations) in the sidebar to see the Integrations overview
  3. Then, select the [Integrations Console](https://vercel.com/d?to=%2Fdashboard%2Fintegrations%2Fconsole&title=Open+Integrations+Console) button and then select Create
  4. Fill out all the entries in the [Create integration form](https://vercel.com/docs/integrations/create-integration#create-integration-form-details) as necessary
  5. At the end of the form, depending on the type of integration you are creating, you must accept the terms provided by Vercel so that your integration can be published
  6. If you are creating a native integration, continue to the [Native integration product creation](https://vercel.com/docs/integrations/create-integration#native-integration-product-creation) process.


###  [Native integration product creation](https://vercel.com/docs/integrations/create-integration#native-integration-product-creation)[](https://vercel.com/docs/integrations/create-integration#native-integration-product-creation)
In order to create native integrations, please share your `team_id` and Integration's [URL Slug](https://vercel.com/docs/integrations/create-integration/submit-integration#url-slug) with Vercel in your shared Slack channel (`#shared-mycompanyname`). You can sign up to be a native integration provider [here](https://vercel.com/marketplace/program).
You can create your product(s) using the [Create product form](https://vercel.com/docs/integrations/create-integration#create-product-form-details) after you have submitted the integration form. Review the [storage product creation flow](https://vercel.com/docs/integrations/create-integration/marketplace-flows#create-a-storage-product-flow) to understand the sequence your integration server needs to handle when a Vercel user installs your product.
###  [Create Integration form details](https://vercel.com/docs/integrations/create-integration#create-integration-form-details)[](https://vercel.com/docs/integrations/create-integration#create-integration-form-details)
The Create Integration form must be completed in full before you can submit your integration for review. The form has the following fields:
Field | Description | Required
---|---|---
[Name](https://vercel.com/docs/integrations/create-integration/submit-integration#integration-name) | The name of your integration. |
[URL Slug](https://vercel.com/docs/integrations/create-integration/submit-integration#url-slug) | The URL slug for your integration. |
[Developer](https://vercel.com/docs/integrations/create-integration/submit-integration#developer) | The owner of the Integration, generally a legal name. |
[Contact Email](https://vercel.com/docs/integrations/create-integration/submit-integration#email) | The contact email for the owner of the integration. This will not be publicly listed. |
[Support Contact Email](https://vercel.com/docs/integrations/create-integration/submit-integration#email) | The support email for the integration. This will be publicly listed. |
[Short Description](https://vercel.com/docs/integrations/create-integration/submit-integration#short-description) | A short description of your integration. |
[Logo](https://vercel.com/docs/integrations/create-integration/submit-integration#logo) | The logo for your integration. |
[Category](https://vercel.com/docs/integrations/create-integration/submit-integration#category) | The category for your integration. |
[Website](https://vercel.com/docs/integrations/create-integration/submit-integration#urls) | The website for your integration. |
[Documentation URL](https://vercel.com/docs/integrations/create-integration/submit-integration#urls) | The documentation URL for your integration. |
[EULA URL](https://vercel.com/docs/integrations/create-integration/submit-integration#urls) | The URL to your End User License Agreement (EULA) for your integration. |
[Privacy Policy URL](https://vercel.com/docs/integrations/create-integration/submit-integration#urls) | The URL to your Privacy Policy for your integration. |
[Overview](https://vercel.com/docs/integrations/create-integration/submit-integration#overview) | A detailed overview of your integration. |
[Additional Information](https://vercel.com/docs/integrations/create-integration/submit-integration#additional-information) | Additional information about configuring your integration. |
[Feature Media](https://vercel.com/docs/integrations/create-integration/submit-integration#feature-media) | A featured image or video for your integration. You can link up to 5 images or videos for your integration with the aspect ratio of 3:2. |
[Redirect URL](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-url) | The URL the user sees during installation. |
[API Scopes](https://vercel.com/docs/integrations/create-integration/submit-integration#api-scopes) | The API scopes for your integration. |
[Webhook URL](https://vercel.com/docs/integrations/create-integration/submit-integration#webhook-url) | The URL to receive webhooks from Vercel. |
[Configuration URL](https://vercel.com/docs/integrations/create-integration/submit-integration#configuration-url) | The URL to configure your integration. |
[Base URL](https://vercel.com/docs/integrations/create-integration/submit-integration#base-url) (Native integration) | The URL that points to your integration server |
[Redirect Login URL](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-login-url) (Native integration) | The URL where the integration users are redirected to when they open your product's dashboard |
[Installation-level Billing Plans](https://vercel.com/docs/integrations/create-integration/submit-integration#installation-level-billing-plans) (Native integration) | Enable the ability to select billing plans when installing the integration |
[Integrations Agreement](https://vercel.com/docs/integrations/create-integration/submit-integration#integrations-agreement) | The agreement to the Vercel terms (which may differ based on the type of integration) |
###  [Create Product form details](https://vercel.com/docs/integrations/create-integration#create-product-form-details)[](https://vercel.com/docs/integrations/create-integration#create-product-form-details)
The Create Product form must be completed in full for at least one product before you can submit your product for review. The form has the following fields:
Field | Description | Required
---|---|---
[Name](https://vercel.com/docs/integrations/create-integration/submit-integration#product-name) | The name of your product. |
[URL Slug](https://vercel.com/docs/integrations/create-integration/submit-integration#product-url-slug) | The URL slug for your product. |
[Short Description](https://vercel.com/docs/integrations/create-integration/submit-integration#product-short-description) | A short description of your product. |
[Short Billing Plans Description](https://vercel.com/docs/integrations/create-integration/submit-integration#product-short-billing-plans-description) | A short description of your billing plan. |
[Metadata Schema](https://vercel.com/docs/integrations/create-integration/submit-integration#product-metadata-schema) | The metadata your product will receive when a store is created or updated. |
[Logo](https://vercel.com/docs/integrations/create-integration/submit-integration#product-logo) | The logo for your product. |
[Tags](https://vercel.com/docs/integrations/create-integration/submit-integration#product-tags) | Tags for the integrations marketplace categories. |
[Guides](https://vercel.com/docs/integrations/create-integration/submit-integration#product-guides) | Getting started guides for specific frameworks. |
[Resource Links](https://vercel.com/docs/integrations/create-integration/submit-integration#product-resource-links) | Resource links such as documentation. |
[Snippets](https://vercel.com/docs/integrations/create-integration/submit-integration#product-snippets) | Add up to 6 code snippets to help users get started with your product. |
[Edge Config Support](https://vercel.com/docs/integrations/create-integration/submit-integration#edge-config-support) | Enable/Disable Experimentation Edge Config Sync |
[Log Drain Settings](https://vercel.com/docs/integrations/create-integration/submit-integration#log-drain-settings) | Configure a Log Drain |
[Checks API](https://vercel.com/docs/integrations/create-integration/submit-integration#checks-api) | Enable/Disable Checks API |
