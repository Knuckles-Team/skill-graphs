##  [Preview branch used as production branch](https://vercel.com/docs/getting-started-with-vercel#preview-branch-used-as-production-branch)[](https://vercel.com/docs/getting-started-with-vercel#preview-branch-used-as-production-branch)
If you have configured a custom Git branch for a domain or an environment variable, it is considered a preview domain and a preview environment variable. Because of this, the Git branch configured for it is considered a [preview branch](https://vercel.com/docs/git#preview-branches).
When configuring the production branch in the project settings, it is not possible to use a preview branch.
If you still want to use this particular Git branch as a production branch, please follow these steps:
  1. Assign your affected domains to the production environment (clear out the Git branch you've defined for them)
  2. Assign your affected environment variables to the production environment (clear out the Git branch you've defined for them)


Afterwards, you can use the Git branch you originally wanted to use as a production branch.
