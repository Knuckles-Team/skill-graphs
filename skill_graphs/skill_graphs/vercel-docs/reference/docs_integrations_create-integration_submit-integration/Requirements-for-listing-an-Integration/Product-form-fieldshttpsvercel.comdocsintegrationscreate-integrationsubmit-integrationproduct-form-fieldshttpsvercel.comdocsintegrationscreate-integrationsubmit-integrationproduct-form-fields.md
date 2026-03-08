##  [Product form fields](https://vercel.com/docs/integrations/create-integration/submit-integration#product-form-fields)[](https://vercel.com/docs/integrations/create-integration/submit-integration#product-form-fields)
###  [Product Name](https://vercel.com/docs/integrations/create-integration/submit-integration#product-name)[](https://vercel.com/docs/integrations/create-integration/submit-integration#product-name)
It's used as the product card title in the Products section of the marketplace integration page.
###  [Product URL Slug](https://vercel.com/docs/integrations/create-integration/submit-integration#product-url-slug)[](https://vercel.com/docs/integrations/create-integration/submit-integration#product-url-slug)
It's used in the integration console for the url slug of the product's detail page.
###  [Product Short Description](https://vercel.com/docs/integrations/create-integration/submit-integration#product-short-description)[](https://vercel.com/docs/integrations/create-integration/submit-integration#product-short-description)
It's used as the product card description in the Products section of the marketplace integration page.
###  [Product Short Billing Plans Description](https://vercel.com/docs/integrations/create-integration/submit-integration#product-short-billing-plans-description)[](https://vercel.com/docs/integrations/create-integration/submit-integration#product-short-billing-plans-description)
It's used as the product card footer description in the Products section of the marketplace integration page and should be less than 30 characters.
###  [Product Metadata Schema](https://vercel.com/docs/integrations/create-integration/submit-integration#product-metadata-schema)[](https://vercel.com/docs/integrations/create-integration/submit-integration#product-metadata-schema)
The [metadata schema](https://vercel.com/docs/integrations/marketplace-product#metadata-schema) controls the product features such as available regions and CPU size, that you want to allow the Vercel customer to customize in the Vercel integration dashboard. It makes the connection with your
###  [Product Logo](https://vercel.com/docs/integrations/create-integration/submit-integration#product-logo)[](https://vercel.com/docs/integrations/create-integration/submit-integration#product-logo)
It's used as the product logo at the top of the Product settings page once the integration user installs this product. If this is not set, the integration logo is used.
###  [Product Tags](https://vercel.com/docs/integrations/create-integration/submit-integration#product-tags)[](https://vercel.com/docs/integrations/create-integration/submit-integration#product-tags)
It's used to help integration users filter and group their installed products on the installed integration page.
###  [Product Guides](https://vercel.com/docs/integrations/create-integration/submit-integration#product-guides)[](https://vercel.com/docs/integrations/create-integration/submit-integration#product-guides)
You are recommended to include links to get started guides for using your product with specific frameworks. Once your product is added by a Vercel user, these links appear on the product's detail page of the user's Vercel dashboard.
###  [Product Resource Links](https://vercel.com/docs/integrations/create-integration/submit-integration#product-resource-links)[](https://vercel.com/docs/integrations/create-integration/submit-integration#product-resource-links)
These links appear under the Resources left side bar on the product's detail page of the user's Vercel dashboard.
###  [Support link](https://vercel.com/docs/integrations/create-integration/submit-integration#support-link)[](https://vercel.com/docs/integrations/create-integration/submit-integration#support-link)
Under the Resources section, Vercel automatically adds a Support link that is a deep link to the provider's dashboard with a query parameter of `support=true` included.
###  [Product Snippets](https://vercel.com/docs/integrations/create-integration/submit-integration#product-snippets)[](https://vercel.com/docs/integrations/create-integration/submit-integration#product-snippets)
These code snippets are designed to be quick starts for the integration user to connect with the installed product with tools such as `cURL` in order to retrieve data and test that their application is working as expected.
You can add up to 6 code snippets to help users get started with your product. These appear at the top of the product's detail page under a Quickstart section with a tab for each code block.
You can include secrets in the following way:
```
import { createClient } from 'acme-sdk';

const client = createClient('https://your-project.acme.com', '{{YOUR_SECRET}}');
```

When integration users view your snippet in the Vercel dashboard, `{{YOUR_SECRET}}` is replaced with a `*` accompanied by a Show Secrets button. The secret value is revealed when they click the button.
If you're using TypeScript or JavaScript snippets, you can use `{{process.env.YOUR_SECRET}}`. In this case, the snippet view in the Vercel dashboard shows `process.env.YOUR_SECRET` instead of a `*` accompanied by the Show Secrets button.
###  [Edge Config Support](https://vercel.com/docs/integrations/create-integration/submit-integration#edge-config-support)[](https://vercel.com/docs/integrations/create-integration/submit-integration#edge-config-support)
When enabled, integration users can choose an [Edge Config](https://vercel.com/docs/edge-config) to access experimentation feature flag data.
###  [Log Drain Settings](https://vercel.com/docs/integrations/create-integration/submit-integration#log-drain-settings)[](https://vercel.com/docs/integrations/create-integration/submit-integration#log-drain-settings)
When enabled, the integration user can configure a Log Drain for the Native integration. Once the `Delivery Format` is chosen, the integration user can define the Log Drain `Endpoint` and `Headers`, which can be replaced with the environment variables defined by the integration.
![Team and project roles relationship diagram](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Flog-drains%2Flogdrain-integration-console-settings-light.png&w=3840&q=75)![Team and project roles relationship diagram](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Flog-drains%2Flogdrain-integration-console-settings-dark.png&w=3840&q=75)Team and project roles relationship diagram
###  [Checks API](https://vercel.com/docs/integrations/create-integration/submit-integration#checks-api)[](https://vercel.com/docs/integrations/create-integration/submit-integration#checks-api)
When enabled, the integration can use the [Checks API](https://vercel.com/docs/checks)
* * *
[ Previous Integration Image Guidelines ](https://vercel.com/docs/integrations/create-integration/integration-image-guidelines)[ Next Upgrade an Integration ](https://vercel.com/docs/integrations/create-integration/upgrade-integration)
Was this helpful?
Send
On this page
  * [Profile](https://vercel.com/docs/integrations/create-integration/submit-integration#profile)
  * [Integration Name](https://vercel.com/docs/integrations/create-integration/submit-integration#integration-name)
  * [URL Slug](https://vercel.com/docs/integrations/create-integration/submit-integration#url-slug)
  * [Developer](https://vercel.com/docs/integrations/create-integration/submit-integration#developer)
  * [Email](https://vercel.com/docs/integrations/create-integration/submit-integration#email)
  * [Short Description](https://vercel.com/docs/integrations/create-integration/submit-integration#short-description)
  * [Logo](https://vercel.com/docs/integrations/create-integration/submit-integration#logo)
  * [Category](https://vercel.com/docs/integrations/create-integration/submit-integration#category)
  * [URLs](https://vercel.com/docs/integrations/create-integration/submit-integration#urls)
  * [Overview](https://vercel.com/docs/integrations/create-integration/submit-integration#overview)
  * [Additional Information](https://vercel.com/docs/integrations/create-integration/submit-integration#additional-information)
  * [Feature media](https://vercel.com/docs/integrations/create-integration/submit-integration#feature-media)
  * [External Integration Settings](https://vercel.com/docs/integrations/create-integration/submit-integration#external-integration-settings)
  * [Redirect URL](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-url)
  * [API Scopes](https://vercel.com/docs/integrations/create-integration/submit-integration#api-scopes)
  * [Webhook URL](https://vercel.com/docs/integrations/create-integration/submit-integration#webhook-url)
  * [Deployment events](https://vercel.com/docs/integrations/create-integration/submit-integration#deployment-events)
  * [Configuration events](https://vercel.com/docs/integrations/create-integration/submit-integration#configuration-events)
  * [Domain events](https://vercel.com/docs/integrations/create-integration/submit-integration#domain-events)
  * [Project events](https://vercel.com/docs/integrations/create-integration/submit-integration#project-events)
  * [Check events](https://vercel.com/docs/integrations/create-integration/submit-integration#check-events)
  * [Configuration URL](https://vercel.com/docs/integrations/create-integration/submit-integration#configuration-url)
  * [Marketplace Integration Settings](https://vercel.com/docs/integrations/create-integration/submit-integration#marketplace-integration-settings)
  * [Base URL](https://vercel.com/docs/integrations/create-integration/submit-integration#base-url)
  * [Redirect Login URL](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-login-url)
  * [Installation-level Billing Plans](https://vercel.com/docs/integrations/create-integration/submit-integration#installation-level-billing-plans)
  * [Usage](https://vercel.com/docs/integrations/create-integration/submit-integration#usage)
  * [Terms of Service](https://vercel.com/docs/integrations/create-integration/submit-integration#terms-of-service)
  * [Integrations Agreement](https://vercel.com/docs/integrations/create-integration/submit-integration#integrations-agreement)
  * [Marketplace installation flow](https://vercel.com/docs/integrations/create-integration/submit-integration#marketplace-installation-flow)
  * [Query parameters for marketplace](https://vercel.com/docs/integrations/create-integration/submit-integration#query-parameters-for-marketplace)
  * [External installation flow](https://vercel.com/docs/integrations/create-integration/submit-integration#external-installation-flow)
  * [Query parameters for external flow](https://vercel.com/docs/integrations/create-integration/submit-integration#query-parameters-for-external-flow)
  * [Deploy button installation flow](https://vercel.com/docs/integrations/create-integration/submit-integration#deploy-button-installation-flow)
  * [Query Parameters for Deploy Button](https://vercel.com/docs/integrations/create-integration/submit-integration#query-parameters-for-deploy-button)
  * [Product form fields](https://vercel.com/docs/integrations/create-integration/submit-integration#product-form-fields)
  * [Product Name](https://vercel.com/docs/integrations/create-integration/submit-integration#product-name)
  * [Product URL Slug](https://vercel.com/docs/integrations/create-integration/submit-integration#product-url-slug)
  * [Product Short Description](https://vercel.com/docs/integrations/create-integration/submit-integration#product-short-description)
  * [Product Short Billing Plans Description](https://vercel.com/docs/integrations/create-integration/submit-integration#product-short-billing-plans-description)
  * [Product Metadata Schema](https://vercel.com/docs/integrations/create-integration/submit-integration#product-metadata-schema)
  * [Product Logo](https://vercel.com/docs/integrations/create-integration/submit-integration#product-logo)
  * [Product Tags](https://vercel.com/docs/integrations/create-integration/submit-integration#product-tags)
  * [Product Guides](https://vercel.com/docs/integrations/create-integration/submit-integration#product-guides)
  * [Product Resource Links](https://vercel.com/docs/integrations/create-integration/submit-integration#product-resource-links)
  * [Support link](https://vercel.com/docs/integrations/create-integration/submit-integration#support-link)
  * [Product Snippets](https://vercel.com/docs/integrations/create-integration/submit-integration#product-snippets)
  * [Edge Config Support](https://vercel.com/docs/integrations/create-integration/submit-integration#edge-config-support)
  * [Log Drain Settings](https://vercel.com/docs/integrations/create-integration/submit-integration#log-drain-settings)
  * [Checks API](https://vercel.com/docs/integrations/create-integration/submit-integration#checks-api)


Copy as MarkdownGive feedbackAsk AI about this page
