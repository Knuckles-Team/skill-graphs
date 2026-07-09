##  [Billing and usage](https://vercel.com/docs/integrations/create-integration/native-integration#billing-and-usage)[](https://vercel.com/docs/integrations/create-integration/native-integration#billing-and-usage)
Billing and usage tracking are crucial aspects of native integrations that are designed to help you create a system of transparent billing based on resource utilization. It enables flexible pricing models and provides users with clear insights into their integration costs.
Concept | Definition
---|---
Resource-level billing | Billing and usage can be tracked separately for each resource.
[Installation-level billing](https://vercel.com/docs/integrations/create-integration/submit-integration#installation-level-billing-plans) | Billing and usage for all resources can also be combined under one installation.
Billing plan and payment | A plan can be of type prepaid or subscription. You ensure that the correct plans are pulled from your backend with your [integration server](https://vercel.com/docs/integrations/marketplace-product#update-your-integration-server) before you submit a product for review.
We recommend you implement resource-level billing, which is the default, to provide users with detailed cost breakdowns and enable more flexible pricing strategies.
