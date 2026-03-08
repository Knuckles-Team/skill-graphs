##  [`x-robots-tag`](https://vercel.com/docs/headers/response-headers#x-robots-tag)[](https://vercel.com/docs/headers/response-headers#x-robots-tag)
Present only on:
  * [Preview deployments](https://vercel.com/docs/deployments/environments#preview-environment-pre-production)
  * Outdated [production deployments](https://vercel.com/docs/deployments). When you [promote a new deployment to production](https://vercel.com/docs/deployments/promoting-a-deployment), the `x-robots-tag` header will be sent to requests for outdated production deployments


We add this header automatically with a value of `noindex` to prevent search engines from crawling your Preview Deployments and outdated Production Deployments, which could cause them to penalize your site for duplicate content.
You can prevent this header from being added to your Preview Deployment by:
  * [Assigning a production domain](https://vercel.com/docs/domains/working-with-domains/assign-domain-to-a-git-branch) to it
  * Disabling it manually [using vercel.json](https://vercel.com/docs/project-configuration#headers)
