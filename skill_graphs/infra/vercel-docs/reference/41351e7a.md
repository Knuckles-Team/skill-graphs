##  [Response](https://vercel.com/docs#response)[](https://vercel.com/docs#response)
200Return the updated resource
idstringRequired
The partner-specific ID of the resource
productIdstringRequired
The partner-specific ID/slug of the product. Example: "redis"
protocolSettingsobjectOptional
+Show 1 properties
billingPlanobjectOptional
The billing plan for the resource. If not set, the resource is billed on installation level.
+Show 17 properties
namestringRequired
User-inputted name for the resource.
metadataobjectRequired
User-inputted metadata based on the registered metadata schema.
statusstringRequired
+Show 7 enum values
notificationobjectOptional
Resource's active notification. Example: { "level": "warn", "title": "Database is nearing maximum planned size" }
+Show 4 properties
