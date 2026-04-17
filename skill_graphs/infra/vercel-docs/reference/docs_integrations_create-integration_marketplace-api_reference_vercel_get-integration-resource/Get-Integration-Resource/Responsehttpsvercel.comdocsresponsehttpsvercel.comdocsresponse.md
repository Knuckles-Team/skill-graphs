##  [Response](https://vercel.com/docs#response)[](https://vercel.com/docs#response)
200Success
idstringRequired
The ID provided by the 3rd party provider for the given resource
internalIdstringRequired
The ID assigned by Vercel for the given resource
namestringRequired
The name of the resource as it is recorded in Vercel
statusstringOptional
The current status of the resource
+Show 7 enum values
productIdstringRequired
The ID of the product the resource is derived from
protocolSettingsobjectOptional
Any settings provided for the resource to support its product's protocols
+Show 1 properties
notificationobjectOptional
The notification, if set, displayed to the user when viewing the resource in Vercel
+Show 4 properties
billingPlanIdstringOptional
The ID of the billing plan the resource is subscribed to, if applicable
metadataobjectOptional
The configured metadata for the resource as defined by its product's Metadata Schema
