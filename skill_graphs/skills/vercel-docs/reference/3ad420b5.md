##  [Managing Password Protection](https://vercel.com/docs/accounts#managing-password-protection)[](https://vercel.com/docs/accounts#managing-password-protection)
You can manage Password Protection through the dashboard, API, or Terraform:
  1. ###  [Go to Project Deployment Protection Settings](https://vercel.com/docs/accounts#go-to-project-deployment-protection-settings)[](https://vercel.com/docs/accounts#go-to-project-deployment-protection-settings)
From your Vercel [dashboard](https://vercel.com/dashboard):
    1. Select the project that you wish to enable Password Protection for
    2. Go to [Deployment Protection](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fdeployment-protection&title=Go+to+Deployment+Protection+settings) in the sidebar
  2. ###  [Manage Password Protection](https://vercel.com/docs/accounts#manage-password-protection)[](https://vercel.com/docs/accounts#manage-password-protection)
From the Password Protection section:
    1. Use the toggle to enable the feature
    2. Select the [deployment environment](https://vercel.com/docs/security/deployment-protection#understanding-deployment-protection-by-environment) you want to protect
    3. Enter a password of your choice
    4. Finally, select Save
All your existing and future deployments will be protected with a password for the project. Next time when you access a deployment, you will be asked to log in by entering the password, which takes you to the deployment. A cookie will then be set in your browser for the deployment URL so you don't need to enter the password every time.
![Enabling Password Protection.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fpassword-protection-light.png&w=1920&q=75)![Enabling Password Protection.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fpassword-protection-dark.png&w=1920&q=75)Enabling Password Protection.


###  [Manage using the API](https://vercel.com/docs/accounts#manage-using-the-api)[](https://vercel.com/docs/accounts#manage-using-the-api)
You can manage Password Protection using the Vercel API endpoint to [update an existing project](https://vercel.com/docs/rest-api/reference/endpoints/projects/update-an-existing-project) with the following body
  * `deploymentType`
    * `prod_deployment_urls_and_all_previews`: Standard Protection
    * `all`: All Deployments
    * `preview`: Only Preview Deployments
  * `password`: Password


```
// enable / update password protection
{
  "passwordProtection": {
    "deploymentType": "prod_deployment_urls_and_all_previews" | "all" | "preview",
    "password": "<password>"
  },
}

// disable password protection
{
  "passwordProtection": null
}
```

###  [Manage using Terraform](https://vercel.com/docs/accounts#manage-using-terraform)[](https://vercel.com/docs/accounts#manage-using-terraform)
You can configure Password Protection using `password_protection` in the `vercel_project` data source in the
* * *
[ Previous APIs & SDKs/ Marketplace Vercel API ](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel)[ Next Sign in with Vercel ](https://vercel.com/docs/sign-in-with-vercel)
Was this helpful?
Send
On this page
  * [Password Protection security considerations](https://vercel.com/docs/accounts#password-protection-security-considerations)
  * [Managing Password Protection](https://vercel.com/docs/accounts#managing-password-protection)
  * [Go to Project Deployment Protection Settings](https://vercel.com/docs/accounts#go-to-project-deployment-protection-settings)
  * [Manage Password Protection](https://vercel.com/docs/accounts#manage-password-protection)
  * [Manage using the API](https://vercel.com/docs/accounts#manage-using-the-api)
  * [Manage using Terraform](https://vercel.com/docs/accounts#manage-using-terraform)


Copy as MarkdownGive feedbackAsk AI about this page
