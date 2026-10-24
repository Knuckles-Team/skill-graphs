##  [Enforcing Code Approvals](https://vercel.com/docs/getting-started-with-vercel#enforcing-code-approvals)[](https://vercel.com/docs/getting-started-with-vercel#enforcing-code-approvals)
Code Approvals by the correct owners are enforced through the `Vercel – Code Owners` GitHub check added by the Vercel GitHub App.
When a pull request is opened, the GitHub App will check if the pull request contains changes to a directory or file that has Code Approvers defined.
If no Code Approvers are defined for the changes then the check will pass. Otherwise, the check will fail until the correct Code Approvers have approved the changes.
To make Code Owners required, follow the `Vercel – Code Owners` as a required check to your repository.
