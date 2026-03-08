##  [Response](https://vercel.com/docs#response)[](https://vercel.com/docs#response)
200The alias information
aliasstringRequired
The alias name, it could be a `.vercel.app` subdomain or a custom domain
createdstringRequired
The date when the alias was created
createdAtnumberOptional
The date when the alias was created in milliseconds since the UNIX epoch
creatorobjectOptional
Information of the user who created the alias
+Show 3 properties
deletedAtnumberOptional
The date when the alias was deleted in milliseconds since the UNIX epoch
deploymentobjectOptional
A map with the deployment ID, URL and metadata
+Show 3 properties
deploymentIdstringRequired
The deployment ID
projectIdstringRequired
The unique identifier of the project
redirectstringOptional
Target destination domain for redirect when the alias is a redirect
redirectStatusCodenumberOptional
Status code to be used on redirect
+Show 4 enum values
uidstringRequired
The unique identifier of the alias
updatedAtnumberOptional
The date when the alias was updated in milliseconds since the UNIX epoch
protectionBypassobjectOptional
The protection bypass for the alias
microfrontendsobjectOptional
The microfrontends for the alias including the routing configuration
+Show 2 properties
