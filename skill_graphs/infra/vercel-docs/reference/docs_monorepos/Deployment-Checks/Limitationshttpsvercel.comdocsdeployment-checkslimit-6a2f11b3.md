##  [Limitations](https://vercel.com/docs/deployment-checks#limitations)[](https://vercel.com/docs/deployment-checks#limitations)
GitHub and GitHub Actions have edge cases with status reporting. These behaviors are matched in GitHub-backed Deployment Checks.
  * To trigger a workflow in response to Vercel deployments using
  * GitHub uses the names of jobs to identify which checks are the same across instances. This means that:
    * Changing the name of a job requires updating your Deployment Checks to align with the names
    * Each run of a GitHub Workflow should result in only one commit status. For example, when using
  * Avoid using the same name for actions across multiple workflows. Due to GitHub's implementation of Check Runs, these will collide and introduce race conditions when used with GitHub branch protection rules, GitHub rulesets, and Vercel Deployment Checks.


* * *
[ Previous Deploy Hooks ](https://vercel.com/docs/deploy-hooks)[ Next Deployment Retention ](https://vercel.com/docs/deployment-retention)
Was this helpful?
Send
On this page
  * [Understanding Deployment Checks](https://vercel.com/docs/deployment-checks#understanding-deployment-checks)
  * [Enabling Deployment Checks](https://vercel.com/docs/deployment-checks#enabling-deployment-checks)
  * [Ensure prerequisites are enabled](https://vercel.com/docs/deployment-checks#ensure-prerequisites-are-enabled)
  * [Select your Deployment Checks](https://vercel.com/docs/deployment-checks#select-your-deployment-checks)
  * [Update workflows (if necessary)](https://vercel.com/docs/deployment-checks#update-workflows-if-necessary)
  * [Create a new production deployment](https://vercel.com/docs/deployment-checks#create-a-new-production-deployment)
  * [Run GitHub Actions to fulfill all Deployment Checks](https://vercel.com/docs/deployment-checks#run-github-actions-to-fulfill-all-deployment-checks)
  * [Promote to production once all Deployment Checks are met](https://vercel.com/docs/deployment-checks#promote-to-production-once-all-deployment-checks-are-met)
  * [Bypassing Deployment Checks](https://vercel.com/docs/deployment-checks#bypassing-deployment-checks)
  * [Limitations](https://vercel.com/docs/deployment-checks#limitations)


Copy as MarkdownGive feedbackAsk AI about this page
Deployment Checks
