##  [Request](https://vercel.com/docs#request)[](https://vercel.com/docs#request)
This endpoint expects an object.
productIdstringRequired
The partner-specific ID/slug of the product. Example: "redis"
namestringRequired
User-inputted name for the resource.
metadataobjectRequired
User-inputted metadata based on the registered metadata schema.
billingPlanIdstringRequired
Partner-provided billing plan. Example: "pro200"
externalIdstringOptional
An partner-provided identifier used to indicate the source of the resource provisioning. In the Deploy Button flow, the `externalId` will equal the `external-id` query parameter.
protocolSettingsobjectOptional
+Show 1 properties
