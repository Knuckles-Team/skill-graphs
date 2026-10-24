##  [Create your product](https://vercel.com/docs/integrations/create-integration/marketplace-product#create-your-product)[](https://vercel.com/docs/integrations/create-integration/marketplace-product#create-your-product)
In this tutorial, you create a storage product for your native integration through the following steps:
  1. ###  [Set up the integration](https://vercel.com/docs/integrations/create-integration/marketplace-product#set-up-the-integration)[](https://vercel.com/docs/integrations/create-integration/marketplace-product#set-up-the-integration)
Before you can create a product, you must have an existing integration. [Create a new Native Integration](https://vercel.com/docs/integrations/create-integration) or use your existing one.
  2. ###  [Deploy the integration server](https://vercel.com/docs/integrations/create-integration/marketplace-product#deploy-the-integration-server)[](https://vercel.com/docs/integrations/create-integration/marketplace-product#deploy-the-integration-server)
In order to deploy the integration server, you should update your integration configuration to set the base URL to the integration server URL:
    1. Select the team you would like to use from the team switcher.
    2. From your [dashboard](https://vercel.com/dashboard), open [Integrations](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fintegrations&title=Go+to+Integrations) in the sidebar and then select the Integrations Console button.
    3. Select the integration you would like to use for the product.
    4. Find the base URL field in the Product section and set it to the integration server URL.
    5. Select Update.
You can use this integration server
  3. ###  [Add a new product](https://vercel.com/docs/integrations/create-integration/marketplace-product#add-a-new-product)[](https://vercel.com/docs/integrations/create-integration/marketplace-product#add-a-new-product)
    1. Select the integration you would like to use for the product from the Integrations Console
    2. Select Create Product from the Products card of the Product section
  4. ###  [Complete the fields and save](https://vercel.com/docs/integrations/create-integration/marketplace-product#complete-the-fields-and-save)[](https://vercel.com/docs/integrations/create-integration/marketplace-product#complete-the-fields-and-save)
You should now see the Create Product form. Fill in the following fields:
    1. Complete the Name, URL Slug, Visibility and Short Description fields
    2. Optionally toggle Disable Resource Renaming to prevent customers from renaming resources after creation. By default, customers can rename resources. Enable this if your platform requires resource names to remain unchanged after provisioning.
    3. Optionally update the following in the [Metadata Schema](https://vercel.com/docs/integrations/create-integration/marketplace-product#metadata-schema) field:
     * Edit the `properties` of the JSON schema to match the options that you are making available through the integration server.
     * Edit and check that the attributes of each property such as `type` matches your requirements.
     * Include the billing plan options that Vercel will send to your integration server when requesting the list of billing plans.
     * Use the Preview Form section to check your JSON schema as you update it.
Review the data collection process shown in the [submit store creation flow](https://vercel.com/docs/integrations/create-integration/marketplace-flows#submit-store-creation) to understand the impact of the metadata schema.
    1. Select Apply Changes
  5. ###  [Update your integration server](https://vercel.com/docs/integrations/create-integration/marketplace-product#update-your-integration-server)[](https://vercel.com/docs/integrations/create-integration/marketplace-product#update-your-integration-server)
Add or update the [Billing](https://vercel.com/docs/integrations/marketplace-api#billing) endpoints in your integration server so that the appropriate plans are pulled from your backend when Vercel calls these endpoints. Review the
Your integration server needs to handle the [billing plan selection flow](https://vercel.com/docs/integrations/create-integration/marketplace-flows#select-billing-plan) and [resource provisioning flow](https://vercel.com/docs/integrations/create-integration/marketplace-flows#submit-store-creation).
  6. ###  [Publish your product](https://vercel.com/docs/integrations/create-integration/marketplace-product#publish-your-product)[](https://vercel.com/docs/integrations/create-integration/marketplace-product#publish-your-product)
To publish your product, you'll need to request for the new product to be approved:
    1. Check that your product integration follows our [review guidelines](https://vercel.com/docs/integrations/create-integration/approval-checklist)
    2. Email
Once approved, Vercel customers can now add your product with the integration and select a billing plan.
