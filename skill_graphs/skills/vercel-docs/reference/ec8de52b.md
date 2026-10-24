##  [Managing Vercel Authentication](https://vercel.com/docs/activity-log#managing-vercel-authentication)[](https://vercel.com/docs/activity-log#managing-vercel-authentication)
Admins and members can enable or disable Vercel Authentication for their team. Hobby teams can also enable or disable for their own projects. Vercel Authentication is managed on a per-project basis.
You can manage Vercel Authentication through the dashboard, API, or Terraform:
###  [Manage using the dashboard](https://vercel.com/docs/activity-log#manage-using-the-dashboard)[](https://vercel.com/docs/activity-log#manage-using-the-dashboard)
  1. ###  [Go to Project Deployment Protection Settings](https://vercel.com/docs/activity-log#go-to-project-deployment-protection-settings)[](https://vercel.com/docs/activity-log#go-to-project-deployment-protection-settings)
From your Vercel [dashboard](https://vercel.com/dashboard):
    1. Select the project that you wish to enable Password Protection for
    2. Go to [Deployment Protection](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fdeployment-protection&title=Go+to+Deployment+Protection+settings) in the sidebar
  2. ###  [Manage Vercel Authentication](https://vercel.com/docs/activity-log#manage-vercel-authentication)[](https://vercel.com/docs/activity-log#manage-vercel-authentication)
From the Vercel Authentication section:
    1. Use the toggle to enable the feature
    2. Select the [deployment environment](https://vercel.com/docs/deployments/environments) you want to protect
    3. Finally, Select Save
All your existing and future deployments will be protected with Vercel Authentication for the project. Next time when you access a deployment, you will be asked to log in with Vercel if you aren't already logged in, you will be redirected to the deployment URL and a cookie will be set in your browser for that deployment URL.
![Enabling Vercel Authentication.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fsso-protection-light.png&w=1920&q=75)![Enabling Vercel Authentication.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fsso-protection-dark.png&w=1920&q=75)Enabling Vercel Authentication.


###  [Manage using the API](https://vercel.com/docs/activity-log#manage-using-the-api)[](https://vercel.com/docs/activity-log#manage-using-the-api)
You can manage Vercel Authentication using the Vercel API endpoint to [update an existing project](https://vercel.com/docs/rest-api/reference/endpoints/projects/update-an-existing-project) with the following body
  * `prod_deployment_urls_and_all_previews`: Standard Protection
  * `all`: All Deployments
  * `preview`: Only Preview Deployments


```
// enable / update Vercel Authentication
{
  "ssoProtection": {
    "deploymentType": "prod_deployment_urls_and_all_previews" | "all" | "preview"
  }
}

// disable Vercel Authentication
{
  "ssoProtection": null
}
```

###  [Manage using Terraform](https://vercel.com/docs/activity-log#manage-using-terraform)[](https://vercel.com/docs/activity-log#manage-using-terraform)
You can configure Vercel Authentication using `vercel_authentication` in the `vercel_project` data source in the
* * *
[ Previous Sign in with Vercel ](https://vercel.com/docs/sign-in-with-vercel)[ Next Deployment Protection ](https://vercel.com/docs/deployment-protection)
Was this helpful?
Send
On this page
  * [Who can access protected deployments?](https://vercel.com/docs/activity-log#who-can-access-protected-deployments)
  * [Access requests](https://vercel.com/docs/activity-log#access-requests)
  * [Vercel Authentication security considerations](https://vercel.com/docs/activity-log#vercel-authentication-security-considerations)
  * [Managing Vercel Authentication](https://vercel.com/docs/activity-log#managing-vercel-authentication)
  * [Manage using the dashboard](https://vercel.com/docs/activity-log#manage-using-the-dashboard)
  * [Go to Project Deployment Protection Settings](https://vercel.com/docs/activity-log#go-to-project-deployment-protection-settings)
  * [Manage Vercel Authentication](https://vercel.com/docs/activity-log#manage-vercel-authentication)
  * [Manage using the API](https://vercel.com/docs/activity-log#manage-using-the-api)
  * [Manage using Terraform](https://vercel.com/docs/activity-log#manage-using-terraform)


Copy as MarkdownGive feedbackAsk AI about this page
