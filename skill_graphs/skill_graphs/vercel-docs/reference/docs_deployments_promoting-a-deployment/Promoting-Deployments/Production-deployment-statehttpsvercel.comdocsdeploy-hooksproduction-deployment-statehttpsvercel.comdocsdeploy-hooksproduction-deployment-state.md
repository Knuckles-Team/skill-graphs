##  [Production deployment state](https://vercel.com/docs/deploy-hooks#production-deployment-state)[](https://vercel.com/docs/deploy-hooks#production-deployment-state)
Your production deployments could be in one of three states:
  * Staged – This means that a commit has been pushed to `main`, but a domain has not been auto-assigned to the deployment. This type of a deployment can be promoted to Current
  * Promoted – This production deployment has been [promoted](https://vercel.com/docs/deploy-hooks#staging-and-promoting-a-production-deployment) from staging. If a deployment has already been promoted in the past, you can't promote it again. If you want to use a previously promoted deployment, you must do a rollback to it
  * Current – This is the production deployment that is aliased to your domain and the one that is currently being served to your users


* * *
[ Previous Builds ](https://vercel.com/docs/builds)[ Next Deployment Checks ](https://vercel.com/docs/deployment-checks)
Was this helpful?
Send
On this page
  * [Instant Rollback](https://vercel.com/docs/deploy-hooks#instant-rollback)
  * [Promote a deployment from preview to production](https://vercel.com/docs/deploy-hooks#promote-a-deployment-from-preview-to-production)
  * [Staging and promoting a production deployment](https://vercel.com/docs/deploy-hooks#staging-and-promoting-a-production-deployment)
  * [CLI](https://vercel.com/docs/deploy-hooks#cli)
  * [Dashboard](https://vercel.com/docs/deploy-hooks#dashboard)
  * [Production deployment state](https://vercel.com/docs/deploy-hooks#production-deployment-state)


Copy as MarkdownGive feedbackAsk AI about this page
