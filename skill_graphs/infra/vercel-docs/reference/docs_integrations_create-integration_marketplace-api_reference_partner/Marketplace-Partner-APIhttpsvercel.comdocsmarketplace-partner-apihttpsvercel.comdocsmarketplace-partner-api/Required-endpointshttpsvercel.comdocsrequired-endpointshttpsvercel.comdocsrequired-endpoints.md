##  [Required endpoints](https://vercel.com/docs#required-endpoints)[](https://vercel.com/docs#required-endpoints)
Every integration must implement these core endpoints:
  * [**Upsert Installation**](https://vercel.com/upsert-installation) — Called when a user installs or updates your integration. You receive installation details and an access token for calling Vercel's API
  * [**Delete Installation**](https://vercel.com/delete-installation) — Called when a user uninstalls your integration. Clean up resources and revoke access
  * [**Update Resource**](https://vercel.com/update-resource) — Called when a user connects a project or adds configuration. Provision resources based on user settings
