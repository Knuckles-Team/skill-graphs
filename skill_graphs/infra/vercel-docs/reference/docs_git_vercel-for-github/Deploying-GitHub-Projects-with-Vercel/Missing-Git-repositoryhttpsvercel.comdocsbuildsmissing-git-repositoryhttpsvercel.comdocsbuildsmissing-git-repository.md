##  [Missing Git repository](https://vercel.com/docs/builds#missing-git-repository)[](https://vercel.com/docs/builds#missing-git-repository)
When you create a new project from a GitHub repository or connect an existing project to one, you need specific permissions. The required permissions depend on whether a personal GitHub account or a GitHub organization
###  [Personal account repositories](https://vercel.com/docs/builds#personal-account-repositories)[](https://vercel.com/docs/builds#personal-account-repositories)
To import or connect a GitHub repository owned by a Owner. This allows Vercel to configure a webhook and automatically deploy your commits. A Collaborator on a personal repository cannot create new Vercel projects from that repository or connect it to existing projects.
###  [Organization repositories](https://vercel.com/docs/builds#organization-repositories)[](https://vercel.com/docs/builds#organization-repositories)
If an organization owns the repository, you need one of the following permissions to import or connect a GitHub repository:
  * Owner of the GitHub organization


OR
  * Member of the GitHub organization _with access to the repository_. If you are a Member of the organization and do not see the repository as an option in Vercel, verify that you have an


If you have access to the repository but are only an
Contact your GitHub organization's Owner(s) to confirm your current role and repository-level access.
