##  [Promote a deployment from preview to production](https://vercel.com/docs/deploy-hooks#promote-a-deployment-from-preview-to-production)[](https://vercel.com/docs/deploy-hooks#promote-a-deployment-from-preview-to-production)
There may be times when you need to promote an existing preview deployment to production, such as when you need to temporarily use a branch that isn't set as the [production branch](https://vercel.com/docs/git#production-branch).
To promote an existing preview deployment to production on Vercel, do the following:
  1. Go to your project's Deployments section in the sidebar. This tab lists all the previously deployed builds
  2. Click the ellipsis (Promote to Production
  3. The popup dialog informs you of which domain(s) will be linked to the build once promoted. To confirm, select Promote to Production

![Option to confirm promote to production.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fdeployment%2Fpromote-to-prod-light.png&w=1080&q=75)![Option to confirm promote to production.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fdeployment%2Fpromote-to-prod-dark.png&w=1080&q=75)Option to confirm promote to production.
If you have different [Environment Variables](https://vercel.com/docs/environment-variables#environments) set for preview and production deployments then the variables used will change from preview to those you have linked to the production environment. You cannot use your preview environment variables in a production deployment
