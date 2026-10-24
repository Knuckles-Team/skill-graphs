##  [Managing Trusted IPs](https://vercel.com/docs/sign-in-with-vercel#managing-trusted-ips)[](https://vercel.com/docs/sign-in-with-vercel#managing-trusted-ips)
You can manage Trusted IPs through the dashboard, API, or Terraform:
###  [Manage using the dashboard](https://vercel.com/docs/sign-in-with-vercel#manage-using-the-dashboard)[](https://vercel.com/docs/sign-in-with-vercel#manage-using-the-dashboard)
  1. ###  [Go to Project Deployment Protection Settings](https://vercel.com/docs/sign-in-with-vercel#go-to-project-deployment-protection-settings)[](https://vercel.com/docs/sign-in-with-vercel#go-to-project-deployment-protection-settings)
From your Vercel [dashboard](https://vercel.com/dashboard):
    1. Select the project that you wish to enable Trusted IPs for
    2. Go to [Deployment Protection](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fdeployment-protection&title=Go+to+Deployment+Protection+settings) in the sidebar
  2. ###  [Manage Vercel Authentication](https://vercel.com/docs/sign-in-with-vercel#manage-vercel-authentication)[](https://vercel.com/docs/sign-in-with-vercel#manage-vercel-authentication)
Ensure Vercel Authentication is enabled. See [Managing Vercel Authentication](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication#managing-vercel-authentication).
  3. ###  [Manage Trusted IPs](https://vercel.com/docs/sign-in-with-vercel#manage-trusted-ips)[](https://vercel.com/docs/sign-in-with-vercel#manage-trusted-ips)
From the Trusted IPs section:
    1. Use the toggle to enable the feature
    2. Select the [deployment environment](https://vercel.com/docs/security/deployment-protection#understanding-deployment-protection-by-environment) you want to protect
    3. Enter your list of IPv4 addresses and IPv4 CIDR ranges with an optional note describing the address
    4. Finally, select Save
All your existing and future deployments will be protected with Trusted IPs for that project. Visitors to your project deployments from IP addresses not included in your list will see a [No Deployment Found](https://vercel.com/docs/errors/platform-error-codes#404:-deployment_not_found) error page.


###  [Manage using the API](https://vercel.com/docs/sign-in-with-vercel#manage-using-the-api)[](https://vercel.com/docs/sign-in-with-vercel#manage-using-the-api)
You can manage Trusted IPs using the Vercel API endpoint to [update an existing project](https://vercel.com/docs/rest-api/reference/endpoints/projects/update-an-existing-project) with the following body
  * `deploymentType`
    * `prod_deployment_urls_and_all_previews`: Standard Protection
    * `all`: All Deployments
    * `preview`: Only Preview Deployments
    * `production`: Only Production Deployments
  * `addresses`: Array of addresses
    * `value`: The IPv4, or IPv4 CIDR address
    * `note`: Optional note about the address
    * `protectionMode`
      * `additional`: IP is required along with other enabled protection methods (recommended setting)
      * `additional`: IP is required along with other enabled protection methods


```
// enable / update trusted ips
{
  "trustedIps": {
      "deploymentType": "all" | "preview" | "production" | "prod_deployment_urls_and_all_previews",
      "addresses": { "value": "<value>"; "note": "<note>" | undefined }[],
      "protectionMode": "additional"
  }
}
// disable trusted ips
{
  "trustedIps": null
}
```

###  [Manage using Terraform](https://vercel.com/docs/sign-in-with-vercel#manage-using-terraform)[](https://vercel.com/docs/sign-in-with-vercel#manage-using-terraform)
You can configure Trusted IPs using `trusted_ips` in the `vercel_project` data source in the
* * *
[ Previous Account Management ](https://vercel.com/docs/accounts)[ Next Getting Started ](https://vercel.com/docs/sign-in-with-vercel/getting-started)
Was this helpful?
Send
On this page
  * [Trusted IPs security considerations](https://vercel.com/docs/sign-in-with-vercel#trusted-ips-security-considerations)
  * [Managing Trusted IPs](https://vercel.com/docs/sign-in-with-vercel#managing-trusted-ips)
  * [Manage using the dashboard](https://vercel.com/docs/sign-in-with-vercel#manage-using-the-dashboard)
  * [Go to Project Deployment Protection Settings](https://vercel.com/docs/sign-in-with-vercel#go-to-project-deployment-protection-settings)
  * [Manage Vercel Authentication](https://vercel.com/docs/sign-in-with-vercel#manage-vercel-authentication)
  * [Manage Trusted IPs](https://vercel.com/docs/sign-in-with-vercel#manage-trusted-ips)
  * [Manage using the API](https://vercel.com/docs/sign-in-with-vercel#manage-using-the-api)
  * [Manage using Terraform](https://vercel.com/docs/sign-in-with-vercel#manage-using-terraform)


Copy as MarkdownGive feedbackAsk AI about this page
