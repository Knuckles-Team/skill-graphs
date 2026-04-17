# Creating & Triggering Deploy Hooks
Last updated September 24, 2025
Deploy Hooks allow you to create URLs that accept HTTP `POST` requests in order to trigger deployments and re-run the [Build Step](https://vercel.com/docs/deployments/configure-a-build). These URLs are uniquely linked to your project, repository, and branch, so there is no need to use any authentication mechanism or provide any payload to the `POST` request.
This feature allows you to integrate Vercel deployments with other systems. For example, you can set up:
  * Automatic deployments on content changes from a Headless CMS
  * Scheduled deployments by configuring third-party cron job services to trigger the Deploy Hook
  * Forced deployments from the command line
