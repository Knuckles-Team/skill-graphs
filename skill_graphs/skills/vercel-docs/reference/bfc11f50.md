# Deployment Checks
Last updated October 9, 2025
Deployment Checks are conditions that must be met before promoting a production build to your production environment.
When a project is connected to GitHub using [Vercel for GitHub](https://vercel.com/docs/git/vercel-for-github), Vercel can automatically read the statuses of your commits and selected GitHub Action results. Using these statuses, Vercel can prevent production deployments from [promoting to production](https://vercel.com/docs/deployments/promoting-a-deployment) until your checks have passed.
