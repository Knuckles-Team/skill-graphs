##  [Native integrations](https://vercel.com/docs/integrations/install-an-integration#native-integrations)[](https://vercel.com/docs/integrations/install-an-integration#native-integrations)
Use this checklist if you're building a [native integration](https://vercel.com/docs/integrations/create-integration/native-integration) that uses the [Marketplace API](https://vercel.com/docs/integrations/create-integration/marketplace-api).
###  [Authentication and setup](https://vercel.com/docs/integrations/install-an-integration#authentication-and-setup)[](https://vercel.com/docs/integrations/install-an-integration#authentication-and-setup)
  * Verify that OAuth and SSO flows authenticate users securely. Test both [Vercel SSO](https://vercel.com/docs/integrations/create-integration/marketplace-api#vercel-initiated-sso) and [Provider SSO](https://vercel.com/docs/integrations/create-integration/marketplace-api#provider-initiated-sso) if applicable.
  * Test the user onboarding flow from Vercel to your platform. Confirm that the [Upsert Installation](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/partner/upsert-installation) endpoint creates and syncs accounts correctly.
  * Confirm that user accounts sync between Vercel and your platform. Use the [Get Account Information](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel/get-account-info) endpoint to retrieve team contact details rather than relying on the installing user's information.


###  [Product listing](https://vercel.com/docs/integrations/install-an-integration#product-listing)[](https://vercel.com/docs/integrations/install-an-integration#product-listing)
  * Validate your product's listing details: name, description, and [logo](https://vercel.com/docs/integrations/create-integration/submit-integration#logo). Confirm the logo is properly centered and looks good in both light and dark mode.
  * Confirm pricing details and plans (free and paid tiers) are accurate. Your [billing plans endpoint](https://vercel.com/docs/integrations/create-integration/marketplace-api#billing) returns the correct plans for each product.
  * Include documentation links (setup guides, FAQs) in your listing. Set the Documentation URL in the integration console.
  * Verify category placement in the Marketplace (for example, AI, Observability, Database) matches your product.
  * Confirm feature parity with your direct offering, including any features tailored for the Marketplace.
  * Ensure your [gallery images](https://vercel.com/docs/integrations/create-integration/submit-integration#feature-media) are high quality (1440x960px, 3:2 ratio) and readable in both light and dark mode. Verify the first image is suitable for the auto-generated Open Graph image.
  * If your integration supports both native and connectable account flows, ensure the connectable account flow works. Otherwise, remove the Redirect URL from the integration console.
  * Add a Marketplace [template](https://vercel.com/docs/deployments/deploy-button/source#store-product-integration) as a deploy option in the product flow. This is required.


###  [Installation and configuration](https://vercel.com/docs/integrations/install-an-integration#installation-and-configuration)[](https://vercel.com/docs/integrations/install-an-integration#installation-and-configuration)
  * Test the installation process for new users who don't have an account on your platform.
  * Test the installation process for existing users who already have an account on your platform.
  * Test the installation from the external flow (user is logged out of Vercel).
  * Confirm that configuration steps (API keys, endpoints, metadata schema options) are clear and functional. Use the Preview Form in the integration console to verify your [metadata schema](https://vercel.com/docs/integrations/create-integration/marketplace-product#metadata-schema) renders correctly.
  * Validate that settings apply correctly after installation. Verify environment variables are set with the correct targets and values.
  * Confirm the uninstall process works and cleans up resources. Handle the [Delete Installation](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/partner/delete-installation) endpoint and return `{finalized: true}` if you don't need a finalization window.
  * Run end-to-end testing: install the integration, provision a resource, connect it to a project, and verify all functionality works as expected.


###  [Feature functionality](https://vercel.com/docs/integrations/install-an-integration#feature-functionality)[](https://vercel.com/docs/integrations/install-an-integration#feature-functionality)
  * Test core features of your product, including query execution, data retrieval, and any product-specific functionality.
  * Verify usage reporting displays correctly in both the Integrations section in the sidebar and the resource dashboard. Confirm that usage charts and stats are formatted properly.
  * Confirm [invoice submission](https://vercel.com/docs/integrations/create-integration/billing#submitting-invoices) works. Submit a test invoice and verify it flows through the expected [lifecycle states](https://vercel.com/docs/integrations/create-integration/billing#invoice-lifecycle).
  * Verify that test snippets and quick-start code blocks appear on the product page. Confirm they include the correct secrets and environment variable references.
  * Publish your Getting Started guide with accurate content and verify it displays correctly.
  * Verify metadata configuration from the integration console: use `vercel-region` controls instead of a generic `select` for region choices, set meaningful default values, and validate controls in both resource creation and update flows.
  * Test the responsiveness of UI elements. Verify buttons, tiles, and dropdowns work as expected.


###  [Billing and usage tracking](https://vercel.com/docs/integrations/install-an-integration#billing-and-usage-tracking)[](https://vercel.com/docs/integrations/install-an-integration#billing-and-usage-tracking)
  * Test your integration against Vercel's [billing system](https://vercel.com/docs/integrations/create-integration/billing). Verify that usage-based pricing calculations are correct.
  * Confirm you [send interim billing data](https://vercel.com/docs/integrations/create-integration/billing#send-interim-billing-data) at least once a day (ideally once per hour) so users see expected charges in their dashboard.
  * Test invoice generation and sync with your billing cycle. Verify that the `period` field aligns with your billing schedule.
  * Test refund processes or billing adjustments using the [Invoice Actions API](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel/update-invoice).
  * Handle `marketplace.invoice.notpaid` and `marketplace.invoice.overdue` webhooks gracefully. Wait at least 15 days before taking destructive actions like deleting resources.


###  [Documentation and support](https://vercel.com/docs/integrations/install-an-integration#documentation-and-support)[](https://vercel.com/docs/integrations/install-an-integration#documentation-and-support)
  * Confirm all setup and usage documentation is complete and accessible at the Documentation URL in the integration console.
  * Test the support contact flow from the marketplace listing page (`/marketplace/[slug]`). This uses the static support link configured in the integration console.
  * Test the support link from the installed product page (`/[teamSlug]/~/integrations/products/[slug]`). This uses an SSO link with the `support=true` query parameter.
  * Test the support link from the resource dashboard page. This also uses an SSO link with the `support=true` query parameter.


###  [Edge cases and scalability](https://vercel.com/docs/integrations/install-an-integration#edge-cases-and-scalability)[](https://vercel.com/docs/integrations/install-an-integration#edge-cases-and-scalability)
  * Simulate high traffic or multiple concurrent installations to test scalability.
  * Test edge cases such as invalid configurations, missing dependencies, or expired tokens.
  * Test [reinstallation behavior](https://vercel.com/docs/integrations/create-integration/native-integration#reinstallation-behavior). If a team uninstalls and reinstalls your integration, verify you treat the new `installationId` as a fresh installation with no assumptions from the previous one.


###  [Next steps for providers](https://vercel.com/docs/integrations/install-an-integration#next-steps-for-providers)[](https://vercel.com/docs/integrations/install-an-integration#next-steps-for-providers)
Once you've completed this checklist:
  1. Email
  2. Vercel reviews your integration and provides feedback or requests additional testing.
  3. Schedule a final walkthrough call to address any remaining questions.
