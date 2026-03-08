##  [Using the Dashboard](https://vercel.com/docs/deployments#using-the-dashboard)[](https://vercel.com/docs/deployments#using-the-dashboard)
Vercel’s dashboard provides a centralized way to view, manage, and gain insights into your deployments.
###  [Resources Tab and Deployment Summary](https://vercel.com/docs/deployments#resources-tab-and-deployment-summary)[](https://vercel.com/docs/deployments#resources-tab-and-deployment-summary)
When you select a deployment from your Project → Deployments page, you can Open Resources in the sidebar to view and search:
  * Middleware: Any configured [matchers](https://vercel.com/docs/routing-middleware/api#match-paths-based-on-custom-matcher-config).
  * Static Assets: Files (HTML, CSS, JS) and their sizes.
  * Functions: The type, runtime, size, and regions.


You can use the three dot (…) menu for a given function to jump to that function in Logs, Analytics, Speed Insights, or the Observability section in the sidebar.
![Example of a deployment resources page with a search applied.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fdeployment-resources-page-light.png&w=3840&q=75)![Example of a deployment resources page with a search applied.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fdeployment-resources-page-dark.png&w=3840&q=75)Example of a deployment resources page with a search applied.
You can also see a summary of these resources by expanding the Deployment Summary section on a Deployment Details page. To visit the Deployment Details page for a deployment, select it from your Project → Deployments page.
![Example of an open deployment summary.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fdeploy-outputs-light.png&w=3840&q=75)![Example of an open deployment summary.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fdeploy-outputs-dark.png&w=3840&q=75)Example of an open deployment summary.
You’ll also see your build time, detected framework, and any relevant logs or errors.
###  [Project Overview](https://vercel.com/docs/deployments#project-overview)[](https://vercel.com/docs/deployments#project-overview)
On your Project Overview page, you can see the latest production deployment, including the generated URL and commit details, and deployment logs for debugging.
###  [Managing Deployments](https://vercel.com/docs/deployments#managing-deployments)[](https://vercel.com/docs/deployments#managing-deployments)
From the Deployments section in the sidebar, you can:
  * Redeploy: Re-run the build for a specific commit or configuration.
  * Inspect: View logs and build outputs.
  * Assign a Custom Domain: Point custom domains to any deployment.
  * Promote to Production: Convert a preview deployment to production (if needed).


For more information on interacting with your deployments, see [Managing Deployments](https://vercel.com/docs/deployments/managing-deployments).
