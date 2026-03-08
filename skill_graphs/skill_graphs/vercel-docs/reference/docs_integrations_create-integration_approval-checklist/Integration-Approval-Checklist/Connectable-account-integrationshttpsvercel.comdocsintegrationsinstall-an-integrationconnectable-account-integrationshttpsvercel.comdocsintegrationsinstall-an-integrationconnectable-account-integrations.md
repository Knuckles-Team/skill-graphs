##  [Connectable account integrations](https://vercel.com/docs/integrations/install-an-integration#connectable-account-integrations)[](https://vercel.com/docs/integrations/install-an-integration#connectable-account-integrations)
Use this checklist if you're building a [connectable account integration](https://vercel.com/docs/integrations/create-integration#connectable-account-integrations) that uses a redirect URL and OAuth flow.
###  [Marketplace listing](https://vercel.com/docs/integrations/install-an-integration#marketplace-listing)[](https://vercel.com/docs/integrations/install-an-integration#marketplace-listing)
Navigate to `/integrations/:slug` to view the listing for your integration.
  * Is the [logo](https://vercel.com/docs/integrations/create-integration/submit-integration#logo) properly centered and cropped? Does it look good in both light and dark mode?


  * Is the first image high-quality and suitable for the auto-generated [Open Graph (OG)](https://vercel.com/docs/og-image-generation) image?
  * Check that none of the images are blurry or display sensitive information. All images should look polished and professional.


Examples:
  * [MongoDB Atlas](https://vercel.com/marketplace/mongodbatlas)
  * [Sanity](https://vercel.com/marketplace/sanity)


###  [Overview and instructions](https://vercel.com/docs/integrations/install-an-integration#overview-and-instructions)[](https://vercel.com/docs/integrations/install-an-integration#overview-and-instructions)
  * Does the description section use markdown where appropriate (for example, `[link](#)`)?
  * If there's an Instructions section, is the content additional and helpful? Avoid a step-by-step installation guide.
  * Do the instructions clearly list all [environment variables](https://vercel.com/docs/integrations/create-integration/submit-integration#additional-information) that get set and what they're used for? Use the [comment property](https://vercel.com/docs/rest-api/endpoints#projects/create-one-or-more-environment-variables/body-parameters) when creating environment variables.
  * Does additional documentation exist? If so, is the documentation URL set?


###  [Installation flow](https://vercel.com/docs/integrations/install-an-integration#installation-flow)[](https://vercel.com/docs/integrations/install-an-integration#installation-flow)
From clicking the install button, a wizard pops up to guide the user through setup.
  * Does the UI offer to select and map Vercel projects with the third-party? Important: The project selection before the popup exists for security reasons. It does not define which projects the user wants to install the integration on.
  * Does the UI preselect the first Vercel project to streamline installation?
  * If a user limits the scope to a single project within Vercel, does the popup respect that? Is the project selection disabled?
  * Are long project names on the project selection handled correctly without breaking the UI?
  * Does the UI include sensible defaults during installation?
  * Are advanced settings hidden behind a toggle? For example, region, RAM, and CPU selections should be preselected and hidden so the UI isn't overloaded with settings.
  * Does the UI use pagination when listing all available projects? Users may have more than the pagination limit of the projects API.
  * Is it impossible for users to exit the installation flow? Links such as the logo or footer should open in a new tab to prevent users from navigating away.
  * Does the authentication flow (sign-up, login, forgotten password) work without interrupting installation? Can the user complete the installation successfully?


###  [Deploy button flow](https://vercel.com/docs/integrations/install-an-integration#deploy-button-flow)[](https://vercel.com/docs/integrations/install-an-integration#deploy-button-flow)
Using [Deploy Buttons](https://vercel.com/docs/deploy-button) allows users to install an integration together with an example repository on GitHub.
  * Does the integration handle the case where it's already installed on the [selected scope](https://vercel.com/docs/integrations/create-integration/submit-integration#deploy-button-installation-flow)? The integration shouldn't treat the passed `configurationId` as a new installation if it was previously installed.


###  [Post-installation](https://vercel.com/docs/integrations/install-an-integration#post-installation)[](https://vercel.com/docs/integrations/install-an-integration#post-installation)
After a user installs your integration through the Marketplace, they should see the details of their installation.
  * Is there a Configuration URL for the integration? Users should be able to modify linked projects by selecting projects in a similar way as during installation.
  * Are the environment variables set correctly with the right target?


* * *
[ Previous Overview ](https://vercel.com/docs/integrations)[ Next Add a Native Integration ](https://vercel.com/docs/integrations/install-an-integration/product-integration)
Was this helpful?
Send
On this page
  * [Native integrations](https://vercel.com/docs/integrations/install-an-integration#native-integrations)
  * [Authentication and setup](https://vercel.com/docs/integrations/install-an-integration#authentication-and-setup)
  * [Product listing](https://vercel.com/docs/integrations/install-an-integration#product-listing)
  * [Installation and configuration](https://vercel.com/docs/integrations/install-an-integration#installation-and-configuration)
  * [Feature functionality](https://vercel.com/docs/integrations/install-an-integration#feature-functionality)
  * [Billing and usage tracking](https://vercel.com/docs/integrations/install-an-integration#billing-and-usage-tracking)
  * [Documentation and support](https://vercel.com/docs/integrations/install-an-integration#documentation-and-support)
  * [Edge cases and scalability](https://vercel.com/docs/integrations/install-an-integration#edge-cases-and-scalability)
  * [Next steps for providers](https://vercel.com/docs/integrations/install-an-integration#next-steps-for-providers)
  * [Connectable account integrations](https://vercel.com/docs/integrations/install-an-integration#connectable-account-integrations)
  * [Marketplace listing](https://vercel.com/docs/integrations/install-an-integration#marketplace-listing)
  * [Overview and instructions](https://vercel.com/docs/integrations/install-an-integration#overview-and-instructions)
  * [Installation flow](https://vercel.com/docs/integrations/install-an-integration#installation-flow)
  * [Deploy button flow](https://vercel.com/docs/integrations/install-an-integration#deploy-button-flow)
  * [Post-installation](https://vercel.com/docs/integrations/install-an-integration#post-installation)


Copy as MarkdownGive feedbackAsk AI about this page
